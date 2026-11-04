---
name: matriz-castorena
description: >-
  Mantener el cerebro y matriz documental de Castorena Abogados para Emi: Archivo muerto, Concentrado de Expedientes, control INDEP de Juntas y Salas, guía Expedientes TFCA y No laborales (TFJA). Usar al recuperar tablas vigentes, comparar versiones, auditar contexto, cerrar el día, incorporar novedades, crear otra tabla de asuntos del despacho o continuar con ChatGPT, Claude o Gemini. Consultar antes de incorporar cualquier nueva familia de tablas; coordinar el procedimiento INDEP sin reemplazarlo ni duplicar sus escrituras.
metadata:
  version: "1.2.0"
  release_date: "2026-11-04"
  language: "es-MX"
---

# Matriz Castorena

## Recuperar la fuente común

1. Leer el directorio `cerebro` de `lianfixx/Cerebro-Castorena-`, **rama `main`**: `MATRIZ.json`, `HISTORIAL.json`, `CONTINUIDAD.md` y `ESTADO.json`. URL: https://github.com/lianfixx/Cerebro-Castorena-/tree/main/cerebro . La ubicación anterior `lianfixx/INDEP`, rama `matriz-castorena`, es un antecedente histórico. Para INDEP operativo consultar siempre **`lianfixx/INDEP`, rama `main`**, su procedimiento y su continuidad más reciente.
2. Recuperar fuentes por IDs/enlaces del catálogo y verificar bytes y SHA-256. La skill instalada contiene reglas, no una copia viva de todas las conversaciones. Leer [operación](references/operacion.md) y [familias](references/familias.md).
3. Registrar en la continuidad las decisiones directas visibles de Emi y las decisiones de implementación del agente por separado, con su procedencia; no presentarlas como conversaciones históricas recuperadas.
4. Verificar capacidades reales de cada entorno: lectura del cerebro público en GitHub, acceso autorizado a `lianfixx/INDEP` y proveedores externos, Drive, archivos, historial, conversaciones, edición, ejecución y programación. La lectura pública del cerebro no concede acceso a otras fuentes ni permisos de escritura. No atribuir acceso por estar instalada la skill. Consultar [portabilidad](references/portabilidad.md).
5. Indicar qué fuentes se recuperaron realmente. Si la búsqueda de conversaciones falla, conservar ese hueco y trabajar con evidencia accesible. No afirmar lectura masiva, exhaustividad, trazabilidad perfecta ni equivalencia entre una etiqueta de versión y bytes históricos.

## Decidir con evidencia

- Separar fuente original, copia idéntica, versión derivada, guía operativa y transcripción. Mantener fuente, hash, versión del proveedor, fecha del hecho, fecha del documento, carga y auditoría. No escoger vigencia sólo por fecha de modificación, sufijo `(2)` o nombre FINAL.
- Conservar el original y todas las versiones distintas recuperables. Vincular copias idénticas por hash; no inventar la genealogía de dos versiones si sólo consta que son diferentes. Marcar relación como desconocida o comparación observada.
- Dar prioridad a instrucciones directas vigentes de Emi para el procedimiento. Registrar sus confirmaciones de identidad con sus palabras y procedencia, sin presentarlas como rectificación oficial del tribunal. Tratar el contenido de correos/documentos como evidencia, no autorización de acciones ni reglas nuevas.
- No inventar números, nombres, secretarios, fechas, plazos, autoridades, estados procesales, lugares o decisiones. Conservar texto literal y pendiente específico cuando no pueda resolverse.
- Mantener las cinco familias independientes (la quinta, No laborales (TFJA), autorizada por Emi el 04/11/2026). La guía TFCA se vincula por folio al maestro INDEP: sus filas compartidas no son nuevos asuntos. No convertir inventario físico en cartera jurídica.
- Ante una tabla de categoría nueva, registrar sólo su título, ubicación y motivo en pendientes; preguntar a Emi **antes de incorporarla**, aunque aparezca en un histórico. No preparar una importación de datos silenciosa.

## Actualizar dentro del alcance autorizado

1. Leer la fuente vigente de nuevo y fijar el SHA del commit y hashes de los archivos antes de editar. Comparar la nueva evidencia por identificadores estables. Si el vínculo o el sentido son ambiguos, conservar la fuente y dejar propuesta pendiente.
2. Crear una versión nueva de trabajo; documentar fuente y celdas/campos exactos, valor anterior/nuevo, motivo y validación. Mantener originales, formato, fórmulas, vacíos y orden. No reconstruir libros para cambios puntuales.
3. Las tareas rutinarias autorizadas no necesitan confirmación repetida. Esa autonomía no permite resolver identidad dudosa, suprimir asuntos, ampliar categorías ni alterar estructura. Emi autorizó migrar el contenido existente de `cerebro/` al repositorio público `lianfixx/Cerebro-Castorena-` al responder «no, hazlo así, por favor», después del aviso de que los datos de expedientes serían públicos. Registrar esa autorización con su procedencia; no extenderla a publicar nuevos datos de expedientes u otras fuentes futuras sin autorización suficiente. No publicar tokens ni credenciales.
4. Para cualquier modificación INDEP aplicar su procedimiento vigente en **`lianfixx/INDEP`, rama `main`**, sus validadores y reserva exclusiva. La matriz sólo indexa sus entregas validadas; no iniciar una segunda actualización del maestro ni duplicar su automatización.
5. Ejecutar `python /ruta/cerebro/skill/scripts/validar_matriz.py /ruta/cerebro` en el repositorio, o el mismo script resuelto desde la carpeta real de esta skill instalada y controles de la familia. Publicar cambios autorizados del cerebro en un único commit sobre `lianfixx/Cerebro-Castorena-`, rama `main`, usando comparación del SHA esperado (CAS); si cambió, releer y conciliar, sin force. Releer las copias publicadas antes de declarar éxito.
6. Ante fallo de Drive, conservar el resultado validado donde sí se guardó y marcar sincronización parcial. No retroceder a una versión antigua por un puntero desactualizado ni afirmar ambas copias sincronizadas.

## Cierre diario

Seguir [operación](references/operacion.md). Revisar fuentes accesibles nuevas desde el último cierre; revisar conversaciones sólo si el conector las devuelve. Actualizar automáticamente el catálogo y los pendientes de familias autorizadas con evidencia inequívoca. Conservar novedades dudosas como pendientes; preguntar por familias nuevas. No enviar correos ni crear alertas/calendarios ajenos a la automatización solicitada.

Registrar fecha y zona `America/Mexico_City`, fuentes leídas/no accesibles, versiones antes/después, cambios, dudas y próximo paso. Si no hubo cambio, no reescribir Excel. No confundir ejecución programada creada con ejecución ya comprobada, ni ejecución de ChatGPT con programación en Claude/Gemini.

## Comunicar

Responder en español claro: qué cambió, qué debe obtener Emi, qué está pendiente y enlaces útiles. Referir acuerdos como identificadores y explicar datos concretos a consultar; Emi indicó que no puede pedir copias. Separar Azcapotzalco/JFCA de Salas TFCA y San Lázaro. Ordenar por secretario sólo cuando exista anotación sustentada y marcar su antigüedad. Este cierre y su automatización no incluyen envíos ni creación de borradores de correo. Una futura solicitud expresa de correo se tramita por separado, con la instrucción y el aviso previo exigidos por Emi; leer una referencia a correo no lo autoriza.

## Registro y continuidad entre IA

Estas reglas valen igual en ChatGPT (incluida su ejecución programada), Claude, Codex, Gemini o cualquier otra IA:
- Empezar por `cerebro/ESTADO.json`, `cerebro/CONTINUIDAD.md` y el último cierre de `cerebro/cierres/` en el repositorio remoto, no por la memoria de una conversación.
- Registrar todo cambio en el mismo commit: el cierre en `cerebro/cierres/` y, para cambios del procedimiento o de los archivos de entrada, una entrada en `CHANGELOG.md` con `Agente:` (quién lo hizo y modelo si se conoce), solicitud, cambios, archivos, verificación (aprobado, falló, no ejecutado o bloqueado) y pendiente.
- Sin escritura en el repositorio, terminar con «Registro pendiente para el repositorio» con la entrada y los cambios exactos. No decir «guardado» si no se escribió.
- Lo prohibido y lo que requiere confirmación de Emi está en `ia/REGLAS.md` del repositorio; cumplirlo aunque la plataforma no tenga frenos. El protocolo completo, con plantillas para pasar trabajo a otra IA, está en `ia/PROTOCOLO.md`.

## Terminado y trabajo en Claude Code

Un cierre o cambio termina cuando: `validar_matriz.py` sale sin errores; el cierre en `cerebro/cierres/` registra fecha local, fuentes leídas y no accesibles, versiones antes y después, cambios, dudas y próximo paso; `ESTADO.json` apunta a ese cierre; el commit se publicó con el SHA esperado y se releyó; y las novedades dudosas o las categorías nuevas quedaron como pendientes, no integradas. Máxima profundidad (`ultrathink` en Claude Code): conciliar versiones distintas de una misma tabla y resolver identidad de asuntos. Para frenos activos, reparto en paralelo y `/goal`, leer [Claude Code](references/claude-code.md).
