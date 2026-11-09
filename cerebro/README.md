# Cerebro Castorena

Punto de continuidad de las siete familias de tablas de Emi. Las versiones vigentes se reflejan en el Escritorio, iCloud y Drive (ver `SINCRONIZACION.json`). Conserva fuentes, versiones, reglas y pendientes sin fusionar universos ni reescribir los Excel originales.

| Familia | Fuente de referencia al cierre inicial | Límite |
|---|---|---|
| Archivo muerto | Catálogo del 28/09/2026: 78 registros físicos | Única versión recuperada; vigencia operativa no confirmada |
| Concentrado | Adjunto 2026-10-29, idéntico a Library v5: 26 registros / 15 hojas | Drive contiene anotación nueva de Alejandra pendiente de conciliar |
| Asuntos INDEP | Maestro lógico v20; última entrega documental 39 | Drive ACTUAL permanece en 18 por sincronización pendiente |
| No laborales (TFJA) | Hoja del control del 05/10/2026: 2 asuntos de INDEP ante el TFJA | Familia desde el 04/11/2026; vigencia por confirmar |
| Expedientes TFCA | Guía v2: 13 folios vinculados al maestro | San Lázaro reúne 3 de esos mismos folios; no suma casos |
| Cotejo Grupo Liverpool | Cotejo físico del 22/10/2026: 50 filas; vivos 9, ganados 33, perdidos 9 | Familia desde el 09/11/2026; el 27969/22-17-02-5 figura como vivo y perdido |
| Cotejo acuses INDEP | Acuses JFCA del 15/10/2026: 12 con partes distintas y 18 con observaciones | Familia desde el 09/11/2026; auxiliar del maestro INDEP, no suma asuntos |

## Abrir los archivos

Las copias preservadas y los enlaces de proveedor están en [MATRIZ.json](MATRIZ.json) y [HISTORIAL.json](HISTORIAL.json). `fuentes/` contiene originales recuperados sin cambios, deduplicados por SHA-256. `evidencia/` conserva la auditoría completa con relaciones y límites. Los archivos históricos no son automáticamente las versiones vigentes.

## Continuar

La ubicación canónica es [lianfixx/Cerebro-Castorena-, rama main, carpeta cerebro](https://github.com/lianfixx/Cerebro-Castorena-/tree/main/cerebro). Leer [AGENTS.md](AGENTS.md), [procedimiento](skill/SKILL.md) y [continuidad](CONTINUIDAD.md). Para otra IA, abrir este directorio en su entorno. CLAUDE.md y GEMINI.md llevan a las mismas reglas. Este destino es público y Emi autorizó expresamente la migración del contenido existente después del aviso sobre su visibilidad; desde el 04/11/2026 también autorizó copiar todas las versiones nuevas y actualizaciones de las cinco familias. Las fuentes externas, la escritura y el programador requieren sus propios permisos y configuración; no se probaron sesiones de Claude/Gemini. INDEP operativo continúa en [lianfixx/INDEP, rama main](https://github.com/lianfixx/INDEP/tree/main), con su procedimiento vigente.

## Actualización diaria

El cierre revisa nuevas fuentes accesibles, compara versiones y guarda evidencia de cambios. Las categorías nuevas quedan pendientes de consulta. INDEP conserva su ejecución y reserva propias; este índice únicamente reconoce sus resultados validados. Ver [ESTADO.json](ESTADO.json) para programación y última cobertura.

## Cobertura inicial

No fue posible leer todas las conversaciones: el servicio de contexto informó que no está disponible. Tampoco se acreditaron todas las versiones internas antiguas de Library. Hay un403 en la primera revisión histórica laboral del concentrado. Estos huecos permanecen explícitos; no hay trazabilidad perfecta declarada.

No se enviaron correos, no se alteraron calendarios y no se modificaron datos de los libros de origen en este cierre.
