#!/usr/bin/env python3
"""Validate MATRIZ.json, HISTORIAL.json and their local evidence snapshots.

Usage: python3 validar_matriz.py /path/to/cerebro
Writes one JSON report to stdout; exits 1 when any validation error occurs.
Only Python's standard library is required. No files are modified.
"""

import hashlib
import json
import re
import sys
from pathlib import Path, PureWindowsPath


FAMILY_IDS = {"archivo_muerto", "concentrado", "indep", "tfca", "no_laborales_tfja", "cotejo_liverpool", "cotejo_acuses_indep"}  # quinta: Emi, 04/11/2026; sexta y séptima: Emi, 09/11/2026
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")


def issue(report, severity, code, location, message):
    report[severity].append({"code": code, "location": location, "message": message})


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Clave JSON duplicada: " + key)
        result[key] = value
    return result


def read_json(root, name, report):
    try:
        with (root / name).open("r", encoding="utf-8-sig") as stream:
            result = json.load(stream, object_pairs_hook=unique_object)
    except (OSError, ValueError, RecursionError) as exc:
        issue(report, "errors", "invalid_document", name, str(exc))
        return None
    if not isinstance(result, dict):
        issue(report, "errors", "invalid_document", name, "Debe ser un objeto JSON.")
        return None
    return result


def get_list(document, key, filename, report, required=True):
    value = document.get(key, None if required else [])
    if not isinstance(value, list):
        issue(report, "errors", "invalid_list", filename + "." + key,
              "Debe ser una lista.")
        return []
    return value


def nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def index_records(records, field, filename, report):
    indexed = {}
    for number, record in enumerate(records):
        location = "{}.{}[{}]".format(filename, field, number)
        if not isinstance(record, dict):
            issue(report, "errors", "invalid_record", location, "Debe ser un objeto.")
            continue
        record_id = record.get("id")
        if not nonempty_string(record_id):
            issue(report, "errors", "invalid_id", location + ".id",
                  "El ID debe ser una cadena no vacía.")
        elif record_id in indexed:
            issue(report, "errors", "duplicate_id", location + ".id",
                  "ID duplicado: " + record_id)
        else:
            indexed[record_id] = record
    return indexed


def check_snapshot(root, record, location, report):
    if "snapshot_path" not in record:
        issue(report, "errors", "missing_snapshot_path", location,
              "Debe incluir snapshot_path, aunque sea null.")
        return
    raw_path = record["snapshot_path"]
    if raw_path is None:
        report["counters"]["snapshots_unavailable"] += 1
        issue(report, "warnings", "snapshot_unavailable", location + ".snapshot_path",
              "Sin copia local; no se pudo cotejar el hash ni el tamaño.")
        return
    if not nonempty_string(raw_path) or "\x00" in raw_path:
        issue(report, "errors", "invalid_snapshot_path", location + ".snapshot_path",
              "Debe ser una ruta relativa no vacía o null.")
        return
    windows_path = PureWindowsPath(raw_path)
    if (Path(raw_path).is_absolute() or windows_path.drive or windows_path.root
            or ".." in raw_path.replace("\\", "/").split("/")):
        issue(report, "errors", "unsafe_snapshot_path", location + ".snapshot_path",
              "No se permiten rutas absolutas, unidades ni segmentos '..'.")
        return
    try:
        resolved = (root / raw_path).resolve(strict=True)
        try:
            resolved.relative_to(root)
        except ValueError:
            issue(report, "errors", "snapshot_outside_root", location + ".snapshot_path",
                  "La ruta resuelta sale del directorio cerebro.")
            return
        if not resolved.is_file():
            raise OSError("El snapshot no es un archivo regular.")
        digest = hashlib.sha256()
        size = 0
        with resolved.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                size += len(chunk)
                digest.update(chunk)
        report["counters"]["snapshots_checked"] += 1
        if digest.hexdigest() != record.get("sha256"):
            issue(report, "errors", "snapshot_hash_mismatch", location + ".sha256",
                  "El SHA-256 del snapshot no coincide con el registrado.")
        if size != record.get("size_bytes"):
            issue(report, "errors", "snapshot_size_mismatch", location + ".size_bytes",
                  "Tamaño real: {}; registrado: {}.".format(size, record.get("size_bytes")))
    except (OSError, ValueError, RuntimeError) as exc:
        issue(report, "errors", "snapshot_unreadable", location + ".snapshot_path", str(exc))


def validate(root, report):
    matrix = read_json(root, "MATRIZ.json", report)
    history = read_json(root, "HISTORIAL.json", report)
    if matrix is None or history is None:
        return
    families = get_list(matrix, "families", "MATRIZ.json", report)
    versions = get_list(history, "versions", "HISTORIAL.json", report)
    family_index = index_records(families, "families", "MATRIZ.json", report)
    version_index = index_records(versions, "versions", "HISTORIAL.json", report)
    report["counters"].update(families=len(families), versions=len(versions))
    missing = sorted(FAMILY_IDS - set(family_index))
    extra = sorted(set(family_index) - FAMILY_IDS)
    if missing or extra:
        issue(report, "errors", "family_scope_mismatch", "MATRIZ.json.families",
              "Familias faltantes: {}; familias adicionales: {}.".format(missing, extra))

    for family_id, family in family_index.items():
        current_id = family.get("current_version_id")
        location = "MATRIZ.json.families[{}].current_version_id".format(family_id)
        if not nonempty_string(current_id) or current_id not in version_index:
            issue(report, "errors", "invalid_current_version", location,
                  "Debe señalar el ID de una versión existente.")
        elif version_index[current_id].get("family_id") != family_id:
            issue(report, "errors", "current_version_wrong_family", location,
                  "La versión vigente pertenece a otra familia.")

    hashes = []
    for number, version in enumerate(versions):
        if not isinstance(version, dict):
            continue
        location = "HISTORIAL.json.versions[{}]".format(number)
        family_id = version.get("family_id")
        if not nonempty_string(family_id) or family_id not in family_index:
            issue(report, "errors", "unknown_version_family", location + ".family_id",
                  "Debe señalar una familia existente en MATRIZ.json.")
        sha256 = version.get("sha256")
        if not isinstance(sha256, str) or not SHA256_RE.fullmatch(sha256):
            issue(report, "errors", "invalid_sha256", location + ".sha256",
                  "Debe contener exactamente 64 caracteres hexadecimales minúsculos.")
        else:
            hashes.append(sha256)
        size = version.get("size_bytes")
        if type(size) is not int or size < 0:
            issue(report, "errors", "invalid_size", location + ".size_bytes",
                  "Debe ser un entero no negativo; booleanos no son válidos.")
        locator = version.get("source_locator")
        if not (nonempty_string(locator) or isinstance(locator, dict) and bool(locator)):
            issue(report, "errors", "invalid_source_locator", location + ".source_locator",
                  "Debe ser una cadena no vacía o un objeto no vacío.")
        if not nonempty_string(version.get("evidence_state")):
            issue(report, "errors", "invalid_evidence_state", location + ".evidence_state",
                  "Debe ser una cadena no vacía.")
        check_snapshot(root, version, location, report)
    report["counters"]["unique_sha256"] = len(set(hashes))
    report["counters"]["repeated_sha256_records"] = len(hashes) - len(set(hashes))

    gaps = get_list(history, "gaps", "HISTORIAL.json", report)
    report["counters"]["gaps"] = len(gaps)
    coverage_complete = history.get("coverage_complete")
    if type(coverage_complete) is not bool:
        issue(report, "errors", "invalid_coverage_complete", "HISTORIAL.json.coverage_complete",
              "Debe ser un booleano.")
    elif gaps and coverage_complete:
        issue(report, "errors", "inconsistent_coverage", "HISTORIAL.json.coverage_complete",
              "Debe ser false cuando gaps contiene pendientes.")

    for filename, document in (("MATRIZ.json", matrix), ("HISTORIAL.json", history)):
        pending = get_list(document, "pending_categories", filename, report, required=False)
        report["counters"]["pending_categories"] += len(pending)
        for number, category in enumerate(pending):
            location = "{}.pending_categories[{}]".format(filename, number)
            if isinstance(category, dict):
                identifiers = [category[key] for key in ("id", "category_id", "family_id")
                               if key in category]
            else:
                identifiers = [category]
            if not identifiers or any(not nonempty_string(value) for value in identifiers):
                issue(report, "errors", "invalid_pending_category", location,
                      "Debe contener un ID, o un objeto con id, category_id o family_id.")
            elif any(value in family_index for value in identifiers):
                issue(report, "errors", "pending_category_integrated", location,
                      "Una categoría pendiente ya figura entre las familias integradas.")


def main(argv=None):
    arguments = sys.argv[1:] if argv is None else argv
    report = {
        "errors": [], "warnings": [],
        "counters": {"families": 0, "versions": 0, "snapshots_checked": 0,
                     "snapshots_unavailable": 0, "unique_sha256": 0,
                     "repeated_sha256_records": 0, "gaps": 0, "pending_categories": 0},
    }
    if len(arguments) != 1:
        issue(report, "errors", "invalid_arguments", "argv",
              "Uso: python3 validar_matriz.py RUTA_AL_DIRECTORIO_CEREBRO")
    else:
        try:
            root = Path(arguments[0]).expanduser().resolve(strict=True)
            if not root.is_dir():
                raise OSError("La ruta cerebro no es un directorio.")
            validate(root, report)
        except (OSError, ValueError, RuntimeError, RecursionError) as exc:
            issue(report, "errors", "invalid_input", "cerebro", str(exc))
    report["counters"]["errors"] = len(report["errors"])
    report["counters"]["warnings"] = len(report["warnings"])
    # Escape even malformed Unicode from external metadata so stdout stays JSON.
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
