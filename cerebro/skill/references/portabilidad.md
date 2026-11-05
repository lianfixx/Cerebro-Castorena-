# Continuar con ChatGPT, Claude o Gemini

Usar `lianfixx/Cerebro-Castorena-`, rama `main`, directorio `cerebro`. Leer `cerebro/AGENTS.md`, `cerebro/skill/SKILL.md`, `cerebro/MATRIZ.json`, `cerebro/HISTORIAL.json`, `cerebro/CONTINUIDAD.md` y `cerebro/ESTADO.json` antes de actuar. Los archivos `CLAUDE.md` y `GEMINI.md` son entradas al mismo procedimiento, no reglas divergentes. El repositorio es público y su contenido existente fue objeto de la migración expresamente autorizada por Emi.

Instrucción inicial sugerida:

> Continúa el cerebro Castorena en lianfixx/Cerebro-Castorena-, rama main, carpeta cerebro. Lee cerebro/AGENTS.md, cerebro/skill/SKILL.md, cerebro/MATRIZ.json, cerebro/HISTORIAL.json, cerebro/CONTINUIDAD.md y cerebro/ESTADO.json. Comprueba conexiones y trabaja sólo con las cinco familias autorizadas. Recupera las fuentes y conserva su trazabilidad. No inventes historial ni incorpores otras tablas sin preguntarme. Para INDEP operativo usa lianfixx/INDEP, rama main, y su procedimiento vigente. Copia al cerebro las versiones validadas nuevas de las cinco familias, conservando las anteriores (autorización de Emi del 04/11/2026).

Comprobar por separado lectura del cerebro público, acceso autorizado a `lianfixx/INDEP`, permisos de escritura en GitHub, lectura/escritura de Drive y archivos, Python3 si hay validación, recuperación de conversaciones y programador. Anotar disponible/no disponible/no probado con evidencia de llamada real. No copiar tokens ni credenciales entre plataformas. Emi autorizó la migración del contenido existente y, desde el 04/11/2026, la copia de todas las versiones nuevas de las cinco familias; otras fuentes requieren consulta. Si falta conexión, pedir acceso mediante el producto o un paquete de los archivos concretos; no prometer sincronización.

La programación de ChatGPT no se traslada a Claude ni Gemini con estos archivos. El ejecutor programado del cierre diario consta en `ESTADO.json` → `executor_current` (desde el 04/11/2026, Claude); la de ChatGPT quedó pausada. Para cambiar de ejecutor, `CAMBIAR_DE_IA.md` del directorio `cerebro/`. Para habilitar allí un ejecutor recurrente se necesita su programador y permisos efectivos; no declarar que funciona sin probarlo. Mantener un único escritor por archivo. La matriz usa publicación atómica con SHA esperado; INDEP usa además su reserva operacional. Si no puede aplicar estos controles, producir propuesta y no escribir.

La compatibilidad es documental y de procedimiento. No se ha ejecutado una sesión real de Claude o Gemini sólo por crear estos adaptadores.
