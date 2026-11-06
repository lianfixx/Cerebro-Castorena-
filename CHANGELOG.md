# Registro de cambios

Lo más reciente arriba. Formato y reglas: `ia/PROTOCOLO.md`, sección 3. Cada entrada lleva la línea `Agente:`.

## 2026-11-05 · tarea programada sin bloqueos de permiso

- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 05/11/2026: que el seguimiento automático funcione.
- Cambios: `TAREA_PROGRAMADA.txt` añade el paso 8: escribir los scripts en archivos y ejecutarlos con `python3`, sin heredocs con llaves y comillas. Las ejecuciones de las 16:02 y 17:04 del 05/11 cotejaron el boletín 192, pero quedaron detenidas por un aviso de permiso antes de registrar y enviar; se interrumpieron sin publicar ni enviar nada.
- Archivos: `cerebro/TAREA_PROGRAMADA.txt` y este registro.
- Verificación: hooks del commit → aprobado.
- Pendiente: ninguno.

## 2026-11-04 · cambiar de ejecutor en cualquier dirección (skill 1.3.1)

- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 04/11/2026: «quiero que todo funcione perfecto, al igual en GEMINI o si decido volver a CHAT GPT».
- Cambios: `cerebro/CAMBIAR_DE_IA.md` (prompts para pausar a la saliente, preparar a Claude, ChatGPT o Gemini y verificar el cambio) y `cerebro/TAREA_PROGRAMADA.txt` (texto común de la tarea programada; no publica si no le toca). `ESTADO.json` → `executor_current` (hoy `claude`). `operacion.md`, `portabilidad.md` y `cerebro/CLAUDE.md` dejan de fijar a Claude como único ejecutor y apuntan al campo y al procedimiento.
- Archivos: `cerebro/CAMBIAR_DE_IA.md`, `cerebro/TAREA_PROGRAMADA.txt`, `cerebro/ESTADO.json`, `cerebro/CLAUDE.md`, `cerebro/skill/` (SKILL.md, operacion.md, portabilidad.md) y este registro.
- Verificación: `validar_matriz.py` → aprobado (0 errores); `ia/test_guard.py` y `ia/check_skill.py` → aprobado.
- Pendiente: que Emi cree la rutina de Claude con ambos repositorios y Google Drive.

## 2026-11-04 · primera ejecución programada de Claude: falló por falta de repositorios

- Agente: Claude Code (sesión en la nube)
- Solicitud: seguimiento propio de la primera ejecución de `trig_01NQu55pefnWfvMFiCWs6Cvc`, encargada por Emi el 4/11/2026.
- Cambios: `ESTADO.json` → `automation_claude` registra el resultado. La ejecución de las 18:43 terminó sin cierre porque la rutina no tiene repositorios ni conectores: push rechazado por el proxy de git e INDEP sin clonar. No se escribió nada. El cierre del día lo hizo ChatGPT a las 18:59 (`cierres/2026-11-04_1859.json`), que además pausó su automatización.
- Archivos: `cerebro/ESTADO.json` y este registro.
- Verificación: `validar_matriz.py` → aprobado (0 errores, 0 avisos); transcripción de la ejecución revisada.
- Pendiente: que Emi cree la rutina desde claude.ai/code con ambos repositorios y Google Drive; borrar después la rutina vieja.

## 2026-11-04 · Claude único ejecutor y copia de todas las versiones (skill 1.3.0)

- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 4/11/2026: «Por ahora solo Claude trabajará, Chat quedará casi inactivo… todas las versiones que hagamos cópialas y todas las tablas y actualizaciones».
- Cambios: maestro INDEP v21 copiado a `cerebro/fuentes/indep/` (bytes idénticos); autorización permanente de copiar las versiones validadas nuevas de las cinco familias, registrada en `MATRIZ.json`, la skill y los README; ya no se pide confirmación para escribir en `cerebro/fuentes/` (siguen inmutables); el cierre diario pasa a Claude a las 18:43 y ChatGPT queda inactivo.
- Archivos: `cerebro/fuentes/indep/6504026c7fa9_…xlsx`, `cerebro/MATRIZ.json`, `cerebro/HISTORIAL.json`, `cerebro/ESTADO.json`, `cerebro/CONTINUIDAD.md`, `cerebro/cierres/`, `cerebro/skill/`, `ia/`, `AGENTS.md`, `README.md`, `cerebro/*.md` y este registro.
- Verificación: `validar_matriz.py` → aprobado (30 fuentes verificadas, 0 errores, 0 avisos); `ia/test_guard.py` → aprobado.
- Pendiente: pausar la ejecución de ChatGPT; observar la primera ejecución de Claude (hoy, 18:43).

## 2026-11-04 · quinta familia «No laborales (TFJA)» y ejecución programada en Claude (skill 1.2.0)

- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 4/11/2026: «Sí por favor» a incorporar «No laborales (TFJA)»; programar una ejecución en Claude.
- Cambios: familia `no_laborales_tfja` en `MATRIZ.json` y `HISTORIAL.json`, con fuente en la hoja ya preservada del 05/10/2026 (2 folios, sin datos nuevos); el validador admite cinco familias; las referencias, `AGENTS.md` y los README hablan de cinco familias; ejecución programada de Claude a las 07:43 (`trig_01NQu55pefnWfvMFiCWs6Cvc`) documentada en `ESTADO.json` y en `operacion.md`.
- Archivos: `cerebro/MATRIZ.json`, `cerebro/HISTORIAL.json`, `cerebro/ESTADO.json`, `cerebro/CONTINUIDAD.md`, `cerebro/skill/` (SKILL.md, referencias y validador), `AGENTS.md`, `cerebro/AGENTS.md`, `README.md`, `cerebro/README.md` y este registro.
- Verificación: `validar_matriz.py` → aprobado (5 familias, 0 errores; 1 aviso esperado por la v21 de INDEP sin copia pública).
- Pendiente: confirmar la vigencia de los folios 82701 y 82702; decidir la copia pública de INDEP v21; observar la primera ejecución de Claude (05/11, 07:43).

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

