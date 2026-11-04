# Operación y trazabilidad

## Secuencia de cierre

1. Leer `MATRIZ.json`, `HISTORIAL.json`, `ESTADO.json` y el cierre anterior de `cerebro` en `lianfixx/Cerebro-Castorena-`, rama `main`.
2. Comprobar conexiones y anotar cobertura. Buscar por títulos, IDs y folios autorizados en GitHub, Library/archivos, Drive y contexto conversacional cuando exista. No hacer búsquedas indiscriminadas en contenidos personales ajenos al despacho.
3. Recuperar todas las páginas de resultados y revisiones expuestas. Para versiones anteriores, descargar y calcular hash: una respuesta con mismo archivo actual y etiqueta vieja no prueba historia recuperada. Conservar archivos de origen, incluidos errores tipográficos.
4. Comparar por contenido y fuente. Una carga reciente de libro viejo no reemplaza una versión validada. Si Drive y adjunto aportan aspectos distintos, mantener ambos y vincular las novedades al registro/celda; no escoger uno íntegro por su fecha.
5. Integrar cambios inequívocos ya autorizados de las cinco familias. Las novedades procesales requieren evidencia del expediente o fuente definida por su procedimiento; una instrucción de buscar algo no confirma que sucedió. Las observaciones de visita deben conservar autor/fecha si constan; si faltan, registrar que faltan.
6. Preservar revisiones originales con snapshot o referencia inmutable verificable. `snapshot_path` debe ser relativo al directorio cerebro; los IDs del proveedor no sustituyen el hash. `coverage_complete` debe permanecer false mientras haya huecos conocidos.
7. Registrar diferencias por campo/celda en evidencia, actualizar punteros sólo después de validar. Un cambio de catálogo puede publicarse sin cambiar ningún Excel.
8. Publicar los cambios autorizados atómicamente en `lianfixx/Cerebro-Castorena-`, rama `main`, con el SHA esperado; no modificar `lianfixx/INDEP`, rama `main`, por esta operación de catálogo. Antes de publicar, comprobar el alcance: la autorización de migrar el contenido existente al destino público no autoriza nuevos datos de expedientes ni otras fuentes futuras. Si hay conflicto, releer estado y cambios ajenos; nunca sobrescribir por fuerza ni reintentar a ciegas. Las escrituras al mismo archivo fuera de GitHub necesitan revisión del proveedor/ETag o reserva equivalente; si no hay control de concurrencia, dejar pendiente.
9. Guardar cierre con cobertura, resultados, límites y candidato de nueva categoría que requiere consulta. No declarar cumplimiento total si hay fuentes inaccesibles.

## Alcance de automatización

Hay dos ejecuciones programadas que se complementan, a horas distintas: Claude a las 07:43 (America/Mexico_City), con acceso a GitHub (matriz e INDEP), y ChatGPT a las 18:30, que además alcanza la Library y el Concentrado de trabajo en Drive. Cada una relee el estado y el último cierre antes de escribir, publica con el SHA esperado y, si encuentra un cambio ajeno, concilia sin force. Nunca deben escribir a la vez: si una detecta trabajo en curso de la otra, deja su resultado como pendiente.

El cierre diario coordina la matriz. La automatización INDEP existente continúa siendo responsable de sus boletines/maestro. La matriz puede actualizar su referencia al último resultado validado; no debe iniciar un cotejo redundante ni enviar otro correo. No alterar una automatización por leer una plantilla que la mencione.

Las instrucciones portables no conceden acceso a conversaciones completas. Un cierre sin acceso a ellas debe decirlo y solicitar exportación o adjuntos sólo si eso impide resolver una necesidad concreta. No solicitar contraseñas, tokens ni acceso público.

## Evidencia mínima de un cambio

Familia y clave; fuente original y hash; hoja/celda o página; valor previo y posterior; fecha del hecho (o desconocida), fecha de captura; autor si consta; nivel de evidencia; operación autorizada; validación; versión resultante; límites. Usar `confirmación de Emi`, `documento leído`, `anotación de tercero`, `hipótesis` o `pendiente`, sin ascender de nivel por repetición.
