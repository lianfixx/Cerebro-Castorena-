#!/usr/bin/env python3
"""Auditoría de fondo de hashes y coherencia del cerebro Castorena. Sin IA.

Uso:  python3 auditar_hashes.py /ruta/a/cerebro [--json informe.json]

Comprueba, sin modificar nada:
  A. Cada archivo de fuentes/ cuyo nombre empieza con 12 hexadecimales: su SHA-256 real
     empieza con ese prefijo.
  B. Cada versión de HISTORIAL.json con snapshot_path: el archivo existe y su SHA-256 y
     tamaño coinciden con lo registrado.
  C. Archivos de fuentes/ que ningún registro menciona (huérfanos).
  D. Cada familia de MATRIZ.json: su versión vigente existe en HISTORIAL.json, los hashes
     coinciden entre sí y el archivo vigente está en fuentes/ con ese hash.
  E. SINCRONIZACION.json: el hash y el tamaño de cada «vigente» son los de la familia.
  F. ESTADO.json contra el último cierre de cierres/: fecha de auditoría y versiones.
  G. Continuidad de cierres/: JSON válido y días sin cierre.

Sale con 1 si hay algún error; los avisos no cambian el código de salida.
Solo usa la biblioteca estándar de Python. No imprime contenido de las tablas.
"""

import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

PREFIJO = re.compile(r"^([0-9a-f]{12})_")
CIERRE = re.compile(r"^(\d{4}-\d{2}-\d{2})_(\d{4})\.json$")
HEX12 = re.compile(r"[0-9a-f]{12}")


def sha256(ruta):
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def leer(ruta, informe):
    try:
        return json.loads(ruta.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        informe["errores"].append({"control": "json", "donde": ruta.name, "detalle": str(exc)})
        return None


def rutas_mencionadas(obj, encontradas):
    """Reúne toda cadena que apunte a fuentes/ dentro de un JSON."""
    if isinstance(obj, dict):
        for v in obj.values():
            rutas_mencionadas(v, encontradas)
    elif isinstance(obj, list):
        for v in obj:
            rutas_mencionadas(v, encontradas)
    elif isinstance(obj, str) and obj.startswith("fuentes/"):
        encontradas.add(obj)


def auditar(raiz):
    informe = {"errores": [], "avisos": [], "conteos": {}}
    err = lambda control, donde, detalle: informe["errores"].append(
        {"control": control, "donde": donde, "detalle": detalle})
    avi = lambda control, donde, detalle: informe["avisos"].append(
        {"control": control, "donde": donde, "detalle": detalle})

    matriz = leer(raiz / "MATRIZ.json", informe) or {}
    historial = leer(raiz / "HISTORIAL.json", informe) or {}
    estado = leer(raiz / "ESTADO.json", informe) or {}
    sinc = leer(raiz / "SINCRONIZACION.json", informe) or {}

    # A. Prefijo del nombre contra el hash real
    reales = {}
    fuentes = raiz / "fuentes"
    for ruta in sorted(p for p in fuentes.rglob("*") if p.is_file()):
        rel = ruta.relative_to(raiz).as_posix()
        reales[rel] = (sha256(ruta), ruta.stat().st_size)
        m = PREFIJO.match(ruta.name)
        if m and not reales[rel][0].startswith(m.group(1)):
            err("A_prefijo", rel, "el nombre dice %s y el archivo es %s" % (m.group(1), reales[rel][0][:12]))
    informe["conteos"]["archivos_en_fuentes"] = len(reales)

    # B. HISTORIAL.versions
    versiones = {}
    con_archivo = 0
    for v in historial.get("versions", []):
        if not isinstance(v, dict):
            continue
        versiones[v.get("id")] = v
        ruta = v.get("snapshot_path")
        if not ruta:
            continue
        if ruta not in reales:
            err("B_version", str(v.get("id")), "falta el archivo " + ruta)
            continue
        con_archivo += 1
        real, tam = reales[ruta]
        if real != v.get("sha256"):
            err("B_version", str(v.get("id")), "hash registrado %s, real %s" % (str(v.get("sha256"))[:12], real[:12]))
        if isinstance(v.get("size_bytes"), int) and v["size_bytes"] != tam:
            err("B_version", str(v.get("id")), "tamaño registrado %s, real %s" % (v["size_bytes"], tam))
    informe["conteos"]["versiones"] = len(versiones)
    informe["conteos"]["versiones_con_archivo"] = con_archivo

    # C. Huérfanos
    mencionadas = set()
    for doc in (matriz, historial, sinc):
        rutas_mencionadas(doc, mencionadas)
    for rel in reales:
        if rel not in mencionadas and not Path(rel).name.startswith("LEEME"):
            avi("C_huerfano", rel, "ningún registro lo menciona")

    # D. MATRIZ.families
    vigentes = {}
    for fam in matriz.get("families", []):
        fid = fam.get("id")
        actual = fam.get("current_version_id")
        h = fam.get("current_sha256") or fam.get("sha256")
        vigentes[fid] = h
        if fam.get("sha256") and fam.get("current_sha256") and fam["sha256"] != fam["current_sha256"]:
            err("D_familia", str(fid), "sha256 y current_sha256 no coinciden")
        if actual not in versiones:
            err("D_familia", str(fid), "la versión vigente %s no está en HISTORIAL.json" % actual)
        elif versiones[actual].get("sha256") != h:
            err("D_familia", str(fid), "la versión vigente tiene otro hash en HISTORIAL.json")
        ruta = fam.get("current_snapshot_path")
        if ruta:
            if ruta not in reales:
                err("D_familia", str(fid), "falta el archivo vigente " + ruta)
            elif reales[ruta][0] != h:
                err("D_familia", str(fid), "el archivo vigente tiene hash %s, se esperaba %s" % (reales[ruta][0][:12], str(h)[:12]))
        else:
            avi("D_familia", str(fid), "sin current_snapshot_path")
    informe["conteos"]["familias"] = len(vigentes)

    # E. SINCRONIZACION.vigentes
    pendientes = 0
    for v in sinc.get("vigentes", []):
        fid = v.get("family_id")
        if fid not in vigentes:
            err("E_sincronizacion", str(fid), "familia desconocida")
            continue
        if v.get("sha256") != vigentes[fid]:
            err("E_sincronizacion", str(fid), "hash %s, la familia tiene %s" % (str(v.get("sha256"))[:12], str(vigentes[fid])[:12]))
        tams = [t for (h, t) in reales.values() if h == v.get("sha256")]
        if tams and isinstance(v.get("size_bytes"), int) and v["size_bytes"] not in tams:
            err("E_sincronizacion", str(fid), "tamaño %s, el archivo mide %s" % (v["size_bytes"], tams[0]))
        if v.get("pendiente_destinos"):
            pendientes += 1
            avi("E_destinos", str(fid), "Drive, Escritorio o iCloud aún sin la versión vigente desde " +
                str(v["pendiente_destinos"].get("desde", "fecha no registrada")))
    informe["conteos"]["familias_con_destinos_pendientes"] = pendientes

    # F y G. Cierres
    cierres = []
    for p in sorted((raiz / "cierres").glob("*.json")):
        m = CIERRE.match(p.name)
        if not m:
            avi("G_cierres", p.name, "nombre fuera del formato AAAA-MM-DD_HHMM.json")
            continue
        doc = leer(p, informe)
        if doc is not None:
            cierres.append((m.group(1), p.name, doc))
    informe["conteos"]["cierres"] = len(cierres)
    if cierres:
        dias = sorted({c[0] for c in cierres})
        d0 = datetime.date.fromisoformat(dias[0])
        d1 = datetime.date.fromisoformat(dias[-1])
        faltan = []
        d = d0
        while d <= d1:
            if d.isoformat() not in dias:
                faltan.append(d.isoformat())
            d += datetime.timedelta(days=1)
        if faltan:
            avi("G_cierres", "cierres/", "días sin cierre: " + ", ".join(faltan))
        fecha, nombre, ultimo = cierres[-1]
        informe["ultimo_cierre"] = nombre
        if estado.get("last_audit_date") != fecha:
            err("F_estado", "ESTADO.json", "last_audit_date es %s y el último cierre es del %s" % (estado.get("last_audit_date"), fecha))
        despues = ultimo.get("versions_after")
        if isinstance(despues, dict):
            for fid, texto in despues.items():
                m = HEX12.search(str(texto))
                if fid in vigentes and m and not str(vigentes[fid]).startswith(m.group(0)):
                    err("F_estado", nombre, "%s: el cierre dice %s y la matriz tiene %s" % (fid, m.group(0), str(vigentes[fid])[:12]))
    else:
        err("G_cierres", "cierres/", "no hay cierres")

    informe["resultado"] = "CON_ERRORES" if informe["errores"] else "CORRECTO"
    return informe


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    informe = auditar(Path(argv[1]))
    texto = json.dumps(informe, ensure_ascii=False, indent=2)
    if "--json" in argv:
        Path(argv[argv.index("--json") + 1]).write_text(texto + "\n", encoding="utf-8")
    print(texto)
    return 1 if informe["errores"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
