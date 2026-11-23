#!/usr/bin/env python3
"""Pruebas de auditar_hashes.py: comprueba que la alarma SÍ suena cuando debe.

Uso: python3 pruebas_auditoria.py /ruta/a/cerebro
Trabaja sobre copias temporales; nunca modifica el cerebro real. Sale con 1 si una prueba falla.
"""

import json
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from auditar_hashes import auditar  # noqa: E402


def copia(origen):
    destino = Path(tempfile.mkdtemp(prefix="cerebro-prueba-")) / "cerebro"
    shutil.copytree(origen, destino)
    return destino


def editar_json(ruta, cambio):
    doc = json.loads(ruta.read_text(encoding="utf-8-sig"))
    cambio(doc)
    ruta.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")


def controles(informe):
    return {e["control"] for e in informe["errores"]}


def caso_limpio(c):
    return auditar(c)["resultado"] == "CORRECTO"


def caso_archivo_alterado(c):
    f = sorted(p for p in (c / "fuentes").rglob("*.xlsx"))[0]
    with f.open("ab") as h:
        h.write(b"x")
    return {"A_prefijo", "B_version"} <= controles(auditar(c))


def caso_archivo_borrado(c):
    doc = json.loads((c / "MATRIZ.json").read_text(encoding="utf-8-sig"))
    (c / doc["families"][0]["current_snapshot_path"]).unlink()
    return {"B_version", "D_familia"} <= controles(auditar(c))


def caso_matriz_hash_cambiado(c):
    def cambio(d):
        d["families"][0]["current_sha256"] = "0" * 64
    editar_json(c / "MATRIZ.json", cambio)
    return "D_familia" in controles(auditar(c))


def caso_sincronizacion_distinta(c):
    def cambio(d):
        d["vigentes"][0]["sha256"] = "f" * 64
    editar_json(c / "SINCRONIZACION.json", cambio)
    return "E_sincronizacion" in controles(auditar(c))


def caso_estado_atrasado(c):
    def cambio(d):
        d["last_audit_date"] = "2000-01-01"
    editar_json(c / "ESTADO.json", cambio)
    return "F_estado" in controles(auditar(c))


def caso_cierre_contradice(c):
    ultimo = sorted((c / "cierres").glob("*.json"))[-1]

    def cambio(d):
        d["versions_after"] = {"indep": "indep-000000000000"}
    editar_json(ultimo, cambio)
    return "F_estado" in controles(auditar(c))


def caso_json_roto(c):
    (c / "HISTORIAL.json").write_text("{roto", encoding="utf-8")
    return "json" in controles(auditar(c))


def caso_huerfano(c):
    (c / "fuentes" / "indep" / "aaaaaaaaaaaa_sin_registro.xlsx").write_bytes(b"x")
    inf = auditar(c)
    return any(a["control"] == "C_huerfano" for a in inf["avisos"]) and "A_prefijo" in controles(inf)


CASOS = [caso_limpio, caso_archivo_alterado, caso_archivo_borrado, caso_matriz_hash_cambiado,
         caso_sincronizacion_distinta, caso_estado_atrasado, caso_cierre_contradice, caso_json_roto,
         caso_huerfano]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    fallos = 0
    for caso in CASOS:
        c = copia(Path(argv[1]))
        try:
            ok = caso(c)
        except Exception as exc:  # una excepción también es un fallo de la alarma
            ok = False
            print("  excepción:", exc)
        finally:
            shutil.rmtree(c.parent, ignore_errors=True)
        print(("OK    " if ok else "FALLO ") + caso.__name__)
        fallos += 0 if ok else 1
    print("%d pruebas, %d fallos" % (len(CASOS), fallos))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
