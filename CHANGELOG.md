# Registro de cambios

Lo más reciente arriba. Formato y reglas: `ia/PROTOCOLO.md`, sección 3. Cada entrada lleva la línea `Agente:`.

## 2026-11-09 · séptima tabla en Drive y sincronización completa

- Agente: Muse (Muse Spark)
- Solicitud: Emi, 09/11/2026: subir «Cotejo acuses INDEP.xlsx» a Drive para cerrar la séptima tabla; verificar 19 925 B y SHA-256 d1c7da59…; registrar en GitHub (base: commit 16865d8 de Claude).
- Cambios: «Cotejo acuses INDEP.xlsx» subido a la carpeta Drive 1UE-tJN2QV1X3eRGokx1pB0PMOW9YKn_z con su nombre fijo, sin conversión; SINCRONIZACION.json (drive_file_id de cotejo_acuses_indep; Drive → sincronizado, sin motivo); cierre cerebro/cierres/2026-11-09_1618.json; ESTADO.json actualizado.
- Archivos: cerebro/SINCRONIZACION.json, cerebro/cierres/2026-11-09_1618.json, cerebro/ESTADO.json, este registro.
- Verificación: SHA-256 y tamaño descargados de vuelta de Drive idénticos a SINCRONIZACION.json (19 925 B, d1c7da59…); validar_matriz.py → aprobado (7 familias, 32 versiones, 0 errores, 0 avisos).
- Pendiente: diferencia 50/51 del Cotejo Liverpool; nota del ID 12 del Concentrado; vigencia de los folios TFJA.

## 2026-11-09 · séptima familia (Cotejo acuses INDEP) y decisión de permisos de Drive

- Agente: Claude Code (claude-opus-5-5, sesión con Emi y Mac enlazada)
- Solicitud: Emi, 09/11/2026 16:04: «1.- No» (conservar el acceso por enlace de Drive), «2.- Sí» (Cotejo acuses INDEP como tabla), «3.- No te entiendo en eso» (diferencia 50/51 de Liverpool).
- Cambios: familia `cotejo_acuses_indep` (d1c7da599e51, 19 925 B) en `MATRIZ.json`, `HISTORIAL.json`, validador, skill 1.5.0, familias, AGENTS, README, CLAUDE, CONTINUIDAD y TAREA_PROGRAMADA; `SINCRONIZACION.json` con la séptima tabla, la decisión de permisos y el nuevo LÉEME; la diferencia de Liverpool queda identificada (27969/22-17-02-5 marcado vivo y perdido). Escritorio e iCloud con la tabla y el LÉEME nuevos; Drive con el LÉEME nuevo (el anterior en «Anteriores»).
- Archivos: `cerebro/MATRIZ.json`, `cerebro/HISTORIAL.json`, `cerebro/ESTADO.json`, `cerebro/SINCRONIZACION.json`, `cerebro/fuentes/cotejo_acuses_indep/d1c7da599e51_Cotejo_acuses_INDEP_2026-10-15.xlsx`, `cerebro/cierres/2026-11-09_1610.json`, `cerebro/skill/SKILL.md`, `cerebro/skill/references/familias.md`, `cerebro/skill/references/operacion.md`, `cerebro/skill/scripts/validar_matriz.py`, `cerebro/AGENTS.md`, `cerebro/README.md`, `cerebro/CLAUDE.md`, `cerebro/CONTINUIDAD.md`, `cerebro/TAREA_PROGRAMADA.txt`, `.claude/skills/matriz-castorena/SKILL.md`, `.agents/skills/matriz-castorena/SKILL.md`, este registro.
- Verificación: `validar_matriz.py` → aprobado (7 familias, 32 versiones, 0 errores); `check_skill.py` → aprobado; SHA-256 en Escritorio, iCloud y LÉEME de Drive → coinciden.
- Pendiente: subir «Cotejo acuses INDEP.xlsx» a Drive (Muse); respuesta de Emi sobre el 27969/22-17-02-5.

## 2026-11-09 · Drive sincronizado y verificado

- Agente: Claude Code (claude-opus-5-5, sesión con Emi y Mac enlazada)
- Solicitud: Emi, 09/11/2026 15:37: «listo», tras el paso de Drive del prompt para Muse.
- Cambios: revisión independiente de la subida de Muse (commit d69fbee): los seis archivos vigentes se descargaron de Drive y coinciden byte a byte con `cerebro/fuentes`; se añadieron el LÉEME (pendiente en el cierre de Muse) y la subcarpeta «Anteriores»; `SINCRONIZACION.json` registra los IDs de Drive y el destino Drive como sincronizado. Se observó que la carpeta hereda acceso «cualquier persona con el enlace puede ver»; no se cambiaron permisos.
- Archivos: `cerebro/SINCRONIZACION.json`, `cerebro/ESTADO.json`, `cerebro/cierres/2026-11-09_1538.json`, este registro.
- Verificación: SHA-256 de 7 archivos en Drive → coinciden; `validar_matriz.py` → aprobado.
- Pendiente: decisión de Emi sobre el acceso por enlace; Cotejo acuses INDEP; diferencia 50/51 de Liverpool.

## 2026-11-09 · tablas vigentes subidas a Drive y verificadas

- Agente: Muse (Muse Spark)
- Solicitud: Emi, 09/11/2026 (encargo por la Mac): subir las tablas vigentes a Drive; Google Drive conectado a Muse.
- Cambios: las 6 tablas vigentes subidas a la carpeta Drive 1UE-tJN2QV1X3eRGokx1pB0PMOW9YKn_z con sus nombres fijos, sin conversión; SINCRONIZACION.json (Drive → sincronizado); cierre cerebro/cierres/2026-11-09_1509.json; ESTADO.json actualizado. El LÉEME no está en GitHub y queda pendiente.
- Archivos: cerebro/SINCRONIZACION.json, cerebro/cierres/2026-11-09_1509.json, cerebro/ESTADO.json, este registro.
- Verificación: SHA-256 de las 6 tablas descargadas de vuelta de Drive idéntico al de SINCRONIZACION.json; validar_matriz.py → aprobado (6 familias, 31 versiones, 0 errores, 0 avisos).
- Pendiente: subir el LÉEME a Drive; integrar «Cotejo acuses INDEP 2026-10-15» como séptima tabla (Emi aprobó el 09/11/2026; falta el archivo, no está en GitHub); diferencia 50/51 del Cotejo Liverpool.

## 2026-11-09 · sexta familia (Cotejo Grupo Liverpool) y sincronización GitHub, Drive e iCloud

- Agente: Claude Code (claude-opus-5-5, sesión con Emi y Mac enlazada)
- Solicitud: Emi, 09/11/2026 14:26 y 14:44: ordenar las tablas del Escritorio con lo vigente a un clic, tenerlo en Drive e iCloud, documentar todo cambio o movimiento en GitHub, Drive e iCloud de forma automática y precisa (también en el cierre y para Muse); «Lo de Cotejo Liverpool es una tabla más».
- Cambios: familia `cotejo_liverpool` (fuente 55e9e955536e, 660 863 B) en `MATRIZ.json`, `HISTORIAL.json` y el validador; nuevo `cerebro/SINCRONIZACION.json` con regla, procedimiento, destinos y nombres fijos; skill 1.4.0 con la sección «Sincronizar GitHub, Drive e iCloud»; operación (paso 7c), familias, AGENTS, README, CONTINUIDAD y TAREA_PROGRAMADA (paso 4b) actualizados. En la Mac: carpeta «Castorena · Tablas» (1 · Vigentes, 2 · Anteriores, 3 · Otras tablas) y en iCloud «Castorena · Tablas vigentes»; originales del Escritorio al basurero tras cotejo por hash. Drive: carpeta creada, archivos pendientes.
- Archivos: `cerebro/MATRIZ.json`, `cerebro/HISTORIAL.json`, `cerebro/ESTADO.json`, `cerebro/SINCRONIZACION.json`, `cerebro/fuentes/cotejo_liverpool/55e9e955536e_Cotejo_Grupo_Liver_confirmados_2.numbers`, `cerebro/cierres/2026-11-09_1450.json`, `cerebro/skill/SKILL.md`, `cerebro/skill/references/familias.md`, `cerebro/skill/references/operacion.md`, `cerebro/skill/scripts/validar_matriz.py`, `cerebro/AGENTS.md`, `cerebro/README.md`, `cerebro/CONTINUIDAD.md`, `cerebro/TAREA_PROGRAMADA.txt`, `.claude/skills/matriz-castorena/SKILL.md`, `.agents/skills/matriz-castorena/SKILL.md`, este registro.
- Verificación: `validar_matriz.py` → aprobado (6 familias, 31 versiones, 0 errores, 0 avisos); `check_skill.py` → aprobado; `test_guard.py` → aprobado; hashes releídos en Escritorio e iCloud → coinciden.
- Pendiente: subir a Drive cuando haya sesión de Google; diferencia 50/51 del Cotejo Liverpool; decidir si «Cotejo acuses INDEP» es tabla.

## 2026-11-09 · cierre diario programado (sin versiones nuevas)

- Agente: Claude Code (ejecución programada)
- Solicitud: tarea programada diaria de la matriz.
- Cambios: cierre `cerebro/cierres/2026-11-09_1843.json`; ESTADO.json actualizado. INDEP sin entrega nueva (última 43); Concentrado sin cambio de metadatos. Ningún Excel reescrito.
- Archivos: `cerebro/cierres/2026-11-09_1843.json`, `cerebro/ESTADO.json`, este registro.
- Verificación: `validar_matriz.py` sin errores.

## 2026-11-07 · cierre diario programado (sin versiones nuevas)

- Agente: Claude Code (ejecución programada)
- Solicitud: tarea programada diaria de la matriz.
- Cambios: cierre `cerebro/cierres/2026-11-07_1843.json`; ESTADO.json actualizado. INDEP sin entrega nueva (última 43); Concentrado sin cambio de metadatos. Ningún Excel reescrito.
- Archivos: `cerebro/cierres/2026-11-07_1843.json`, `cerebro/ESTADO.json`, este registro.
- Verificación: `validar_matriz.py` sin errores.

## 2026-11-06 · cierre diario programado (sin versiones nuevas)

- Agente: Claude Code (ejecución programada)
- Solicitud: tarea programada diaria de la matriz.
- Cambios: cierre `cerebro/cierres/2026-11-06_1844.json`; ESTADO.json actualizado. INDEP entrega 43 sin Excel nuevo (manifiesto verificado); Concentrado sin cambio de metadatos. Ningún Excel reescrito.
- Archivos: `cerebro/cierres/2026-11-06_1844.json`, `cerebro/ESTADO.json`, este registro.
- Verificación: `validar_matriz.py` sin errores.

## 2026-11-06 · integración automática de las tareas programadas

- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 05-06/11/2026: que el seguimiento automático funcione; la opción de subir a cualquier rama no aparece en su pantalla.
- Cambios: workflow `.github/workflows/integrar-tareas.yml`: integra en main las ramas «claude/…» de las tareas programadas si todos sus commits llevan `IA-Actor: … (ejecución programada)` y pasan las reglas de `ia/` de main; si hay conflicto o falla, queda en rojo sin integrar. `.gitattributes` une las entradas de CHANGELOG al integrar. `cerebro/TAREA_PROGRAMADA.txt` explica el procedimiento.
- Archivos: `.github/workflows/integrar-tareas.yml`, `.gitattributes`, `cerebro/TAREA_PROGRAMADA.txt` y este registro.
- Verificación: prueba en copia con la rama del cierre del 05/11 → trailer reconocido, `verificar.py ci` correcto, integración sin conflicto.
- Pendiente: observar la primera integración real (INDEP, 06/11 9:04).

## 2026-11-05 · cierre diario programado (sin versiones nuevas)

- Agente: Claude Code (ejecución programada)
- Solicitud: tarea programada diaria de la matriz.
- Cambios: `cerebro/cierres/2026-11-05_1844.json` y `ESTADO.json`. Sin versiones nuevas ni Excel reescritos; entrega 42 de INDEP verificada con su manifiesto.
- Archivos: `cerebro/cierres/2026-11-05_1844.json`, `cerebro/ESTADO.json` y este registro.
- Verificación: `validar_matriz.py` → 0 errores, 0 avisos.
- Pendiente: hash del Concentrado de Drive; carpeta nueva «INDEP ASUNTO ESTUDIO LIC» sin incorporar.
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

