# Cerebro Castorena

Matriz documental de Emi para Castorena Abogados. Aquí están las cinco tablas de referencia, las versiones recuperadas, las reglas de trabajo y los pendientes.

## Abrir las tablas

Estas son las referencias vigentes al **4 de noviembre de 2026**. Los Excel se descargan desde su página con **Download raw file**.

| Tabla | Alcance y estado de la referencia |
|---|---|
| [Archivo muerto](cerebro/fuentes/archivo_muerto/8305a4b41f43_Catalogo_Archivo_Muerto.xlsx) | 78 registros físicos; única candidata recuperada, vigencia operativa por confirmar. |
| [Concentrado de expedientes](cerebro/fuentes/concentrado/7cbaad8795b9_Concentrado_de_Expedientes_2026-10-29.xlsx) | 26 registros / 15 hojas; referencia del 29/10/2026. Anotación de ID 12 pendiente. |
| [INDEP (Juntas/Salas)](cerebro/fuentes/indep/6504026c7fa9_Control_de_expedientes_Junta_Especial_2-4.xlsx) | Maestro lógico v21, 45 folios; indexado hasta la entrega 42 (04/11/2026). |
| [No laborales (TFJA)](cerebro/fuentes/indep/a52c4946e09d_Control_de_expedientes_Junta_Especial_2_C_1_.xlsx) | 2 asuntos no laborales de INDEP ante el TFJA (hoja «No laborales (TFJA)»), corte 05/10/2026; vigencia por confirmar. |
| [Expedientes TFCA](cerebro/fuentes/tfca/d9e1dcc79a77_Expedientes_TFCA_y_San_Lazaro.xlsx) | Guía v2 de 13 folios del maestro; San Lázaro no agrega casos. |

## Continuar el trabajo

- [Reglas y procedimiento](cerebro/skill/SKILL.md)
- [Matriz: fuentes y versiones seleccionadas](cerebro/MATRIZ.json)
- [Historial: 28 archivos fuente preservados](cerebro/HISTORIAL.json)
- [Contexto y pendientes](cerebro/CONTINUIDAD.md)
- [Estado del cierre diario](cerebro/ESTADO.json)
- [Registro del traslado y verificación](cerebro/MIGRACION.json)
- [Todas las fuentes originales](cerebro/fuentes/)
- [Continuar con ChatGPT, Claude o Gemini](cerebro/skill/references/portabilidad.md)

**Ubicación de la matriz:** este repositorio, rama `main`, carpeta `cerebro/`. **INDEP operativo:** [lianfixx/INDEP, main](https://github.com/lianfixx/INDEP/tree/main), con sus permisos propios. El cierre de la matriz indexa sus entregas validadas y no duplica su operación.

Los huecos históricos y discrepancias permanecen identificados. No se afirma haber leído todas las conversaciones, recuperado todas las versiones ni probado ejecución en Claude/Gemini. La guía TFCA no aumenta el universo del maestro. Cualquier categoría adicional requiere consulta a Emi.

Este traslado conserva los originales y no cambia celdas, fórmulas, estados procesales ni asignaciones. La ubicación pública fue elegida expresamente por Emi para el contenido existente y, desde el 04/11/2026, para todas las versiones nuevas de las cinco tablas.
