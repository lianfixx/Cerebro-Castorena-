# Trabajo en Claude Code

## Frenos activos (hooks)

Solo actúan en Claude Code dentro de este repositorio. No sustituyen las reglas de la skill. Las mismas reglas están en `ia/REGLAS.md` para cualquier IA; con terminal, `sh ia/instalar.sh` (o `python3 ia/verificar.py inicio`) las activa como hooks de git, y GitHub revisa cada push con `registro-ia.yml`.

- Se bloquea cualquier correo o borrador de Gmail: esta matriz no envía.
- Se pide confirmación antes de escribir en `cerebro/fuentes/`: el repositorio es público y la autorización de Emi cubre solo el contenido ya migrado.
- Las fuentes originales de `cerebro/fuentes/` no se modifican ni se borran, tampoco por git o por conector.
- Antes de cada commit que toque `cerebro/` corre `validar_matriz.py`, y se buscan secretos y datos personales en el diff.
- Se pide confirmación antes de `git push`; se bloquean el push forzado y `--no-verify`.
- Todo commit lleva su registro (cierre o `CHANGELOG.md` con `Agente:`).

## Plan y entrevista

Modo plan (Shift+Tab) para un cambio de procedimiento o una conciliación difícil. No hay entrevista en el cierre diario. Ante una categoría nueva no se entrevista: se registra título, ubicación y motivo y se pregunta a Emi si la incorpora.

## Reparto en paralelo

Un subagente de solo lectura por familia (Archivo muerto, Concentrado, INDEP, TFCA) para revisar fuentes nuevas y comparar versiones con hash. Solo el consolidador edita `MATRIZ.json`, `HISTORIAL.json`, `ESTADO.json` y el cierre, y publica. Ningún subagente modifica INDEP: su operación es de `lianfixx/INDEP`.

## /goal

`/goal cierre del día: validar_matriz.py sin errores, cierre guardado en cerebro/cierres con cobertura real, ESTADO.json actualizado, commit publicado y releído`

## En la sesión

- `/context` si la sesión se llena con fuentes grandes.
- `/compact conserva familia, hashes y pendientes` antes de seguir con otra familia.
- `!python3 cerebro/skill/scripts/validar_matriz.py cerebro` para validar sin rodeos.
