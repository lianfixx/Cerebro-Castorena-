# Registro de cambios

Lo más reciente arriba. Formato y reglas: `ia/PROTOCOLO.md`, sección 3. Cada entrada lleva la línea `Agente:`.

## 2026-11-04 · matriz-castorena 1.1.0 bajo el protocolo común entre IA

- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 4/11/2026: revisar la skill, aplicar solo las mejoras necesarias, ponerla bajo las mismas reglas que los demás repositorios y dejarla lista para instalar.
- Cambios: skill 1.1.0 con versión en metadatos, sección «Registro y continuidad entre IA» y criterio de terminado; `references/claude-code.md` nuevo. Capa común `ia/`, que incluye frenos propios: sin correos ni borradores, confirmación antes de escribir en `cerebro/fuentes/` por ser público, fuentes originales inmutables y `validar_matriz.py` antes de cada commit sobre `cerebro/`. Workflow `registro-ia.yml`, puentes `.claude/skills/` y `.agents/skills/`, secciones en `AGENTS.md`, `CLAUDE.md` y `GEMINI.md`. El método, las cuatro familias, los Excel y los JSON de la matriz no cambian.
- Archivos: `cerebro/skill/SKILL.md`, `cerebro/skill/references/claude-code.md`, `cerebro/CONTINUIDAD.md`, `ia/`, `.claude/`, `.agents/`, `.github/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` y este registro.
- Verificación: `python3 cerebro/skill/scripts/validar_matriz.py cerebro` → aprobado (0 errores, 28 snapshots); `python3 ia/test_guard.py` → aprobado; `python3 ia/check_skill.py` → aprobado; YAML de la skill y de los puentes → aprobado.
- Pendiente: decisión de Emi sobre la visibilidad pública del repositorio (ver `cerebro/CONTINUIDAD.md`).

## 2026-11-04 · corrección: puentes de skill con YAML válido

- Agente: Claude Code (sesión en la nube)
- Solicitud: autocorrección de Claude Code al revisar la skill matriz-castorena (4/11/2026).
- Cambios: los puentes `.claude/skills/` y `.agents/skills/` copiaban la descripción sin comillas; si contenía «: » el YAML quedaba inválido (afectaba a tareas-maestria y meta-ads-client-onboarding). Ahora va entre comillas, `ia/check_skill.py` rechaza valores que rompan el YAML y el control previo al commit revisa también los puentes.
- Archivos: `ia/check_skill.py`, `ia/politica.json`, `ia/REGLAS.md`, puentes de skill (si existen) y este registro.
- Verificación: `python3 ia/test_guard.py` → aprobado; `python3 ia/verificar.py inicio` → aprobado.
- Pendiente: ninguno.

