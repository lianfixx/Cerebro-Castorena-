# Operación y trazabilidad

## Secuencia de cierre

1. Leer `MATRIZ.json`, `HISTORIAL.json`, `ESTADO.json` y el cierre anterior de `cerebro` en `lianfixx/Cerebro-Castorena-`, rama `main`.
2. Comprobar conexiones y anotar cobertura. Buscar por títulos, IDs y folios autorizados en GitHub, Library/archivos, Drive y contexto conversacional cuando exista. No hacer búsquedas indiscriminadas en contenidos personales ajenos al despacho.
3. Recuperar todas las páginas de resultados y revisiones expuestas. Para versiones anteriores, descargar y calcular hash: una respuesta con mismo archivo actual y etiqueta vieja no prueba historia recuperada. Conservar archivos de origen, incluidos errores tipográficos.
4. Comparar por contenido y fuente. Una carga reciente de libro viejo no reemplaza una versión validada. Si Drive y adjunto aportan aspectos distintos, mantener ambos y vincular las novedades al registro/celda; no escoger uno íntegro por su fecha.
5. Integrar cambios inequívocos ya autorizados de las cinco familias. Las novedades procesales requieren evidencia del expediente o fuente definida por su procedimiento; una instrucción de buscar algo no confirma que sucedió. Las observaciones de visita deben conservar autor/fecha si constan; si faltan, registrar que faltan.
6. Preservar revisiones originales con snapshot o referencia inmutable verificable. `snapshot_path` debe ser relativo al directorio cerebro; los IDs del proveedor no sustituyen el hash. `coverage_complete` debe permanecer false mientras haya huecos conocidos.
7. Registrar diferencias por campo/celda en evidencia, actualizar punteros sólo después de validar. Un cambio de catálogo puede publicarse sin cambiar ningún Excel.
7b. Copiar a `fuentes/<familia>/` cada versión validada nueva (nombre `<12 primeros del SHA-256>_<nombre original>`), registrar su versión en `HISTORIAL.json` y apuntar la familia a ella en `MATRIZ.json`; nunca sobrescribir ni borrar una fuente anterior.
8. Publicar los cambios autorizados atómicamente en `lianfixx/Cerebro-Castorena-`, rama `main`, con el SHA esperado; no modificar `lianfixx/INDEP`, rama `main`, por esta operación de catálogo. Antes de publicar, comprobar el alcance: copiar al cerebro las versiones validadas nuevas de las cinco familias está autorizado por Emi desde el 04/11/2026; fuentes de otras categorías siguen requiriendo consulta. Si hay conflicto, releer estado y cambios ajenos; nunca sobrescribir por fuerza ni reintentar a ciegas. Las escrituras al mismo archivo fuera de GitHub necesitan revisión del proveedor/ETag o reserva equivalente; si no hay control de concurrencia, dejar pendiente.
9. Guardar cierre con cobertura, resultados, límites y candidato de nueva categoría que requiere consulta. No declarar cumplimiento total si hay fuentes inaccesibles.

## Alcance de automatización

Un solo ejecutor a la vez, indicado en `ESTADO.json` → `executor_current` (`claude`, `chatgpt`, `gemini` o `null` durante un cambio). Desde el 04/11/2026, por decisión de Emi, es Claude (18:43, America/Mexico_City; ver `automation_claude`); la ejecución de ChatGPT («Cerrar matriz Castorena», 18:30) quedó pausada y verificada. Para cambiar de ejecutor en cualquier dirección, seguir `CAMBIAR_DE_IA.md`; la tarea programada de cualquier IA usa `TAREA_PROGRAMADA.txt`, que no publica si `executor_current` no es su id. Si dos ejecuciones coinciden, releer el estado, publicar con el SHA esperado y conciliar sin force. Claude no alcanza la Library de ChatGPT; el Concentrado de trabajo en Drive solo es accesible si la tarea tiene el conector de Drive y el archivo está compartido con la cuenta de Emi. Lo inaccesible se anota en cada cierre.

El cierre diario coordina la matriz. La automatización INDEP existente continúa siendo responsable de sus boletines/maestro. La matriz puede actualizar su referencia al último resultado validado; no debe iniciar un cotejo redundante ni enviar otro correo. No alterar una automatización por leer una plantilla que la mencione.

Las instrucciones portables no conceden acceso a conversaciones completas. Un cierre sin acceso a ellas debe decirlo y solicitar exportación o adjuntos sólo si eso impide resolver una necesidad concreta. No solicitar contraseñas, tokens ni acceso público.

## Evidencia mínima de un cambio

Familia y clave; fuente original y hash; hoja/celda o página; valor previo y posterior; fecha del hecho (o desconocida), fecha de captura; autor si consta; nivel de evidencia; operación autorizada; validación; versión resultante; límites. Usar `confirmación de Emi`, `documento leído`, `anotación de tercero`, `hipótesis` o `pendiente`, sin ascender de nivel por repetición.
