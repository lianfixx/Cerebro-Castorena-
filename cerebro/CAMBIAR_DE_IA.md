# Cambiar la IA que hace el cierre diario de la matriz

Sirve para pasar el cierre diario entre Claude, ChatGPT, Gemini u otra IA, en cualquier dirección. La
skill, las reglas y el validador son los mismos para todas.

**Regla de oro:** un solo ejecutor a la vez. Quién es consta en `ESTADO.json` → `executor_current`
(`claude`, `chatgpt`, `gemini` o `null` durante un cambio). `TAREA_PROGRAMADA.txt` es el texto de la
tarea programada para cualquier IA: si `executor_current` no es su id, no publica nada.

La matriz no manda correos. El seguimiento de INDEP se cambia aparte, con `CAMBIAR_DE_IA.md` de
`lianfixx/INDEP`.

## Pasos (siempre en este orden)

1. **Pausar la IA saliente:** pega el prompt 1 en la IA que deja de trabajar.
2. **Preparar la IA entrante:** sigue la sección de esa IA (2A, 2B o 2C).
3. **Verificar el cambio:** pega el prompt 3 en la IA entrante, o pídeselo a Claude Code.

### Prompt 1 · Pausar la IA saliente

```
Vas a dejar de hacer el cierre diario de la matriz Castorena (lianfixx/Cerebro-Castorena-, rama main). Lee AGENTS.md, ia/REGLAS.md y cerebro/CAMBIAR_DE_IA.md y cúmplelos. No envíes correos.

1. Pausa tu tarea o automatización programada del cierre de la matriz. No la borres. Confirma su nombre, su ID y que quedó en pausa, y que no tienes otra activa de la matriz.
2. En cerebro/ESTADO.json registra tu tarea como pausada y pon executor_current en null. Valida con `python3 cerebro/skill/scripts/validar_matriz.py cerebro`, haz un commit con la línea «Agente:» y el trailer «IA-Actor:», comprueba el SHA esperado y nunca uses force.
3. Dame un resumen corto y el commit publicado.
```

### 2A · Si entra Claude

1. En el navegador, abre **claude.ai/code → Rutinas → Nueva rutina**.
2. Repositorios: **lianfixx/Cerebro-Castorena-** y **lianfixx/INDEP**. Conector: **Google Drive**.
3. Horario: todos los días a las 18:43 (Ciudad de México).
4. Instrucciones: pega el contenido completo de `cerebro/TAREA_PROGRAMADA.txt`.

### 2B · Si vuelve ChatGPT

1. En ChatGPT, **reanuda** la tarea «Cerrar matriz Castorena» (ID `6aea5a544e288191994d562d5d075090`).
   Si ya no existe, crea una nueva a la misma hora.
2. Comprueba que tenga GitHub (los dos repositorios) y Google Drive.
3. Sustituye sus instrucciones por el contenido completo de `cerebro/TAREA_PROGRAMADA.txt`.
4. En Claude, abre claude.ai/code → Rutinas y **pausa** la rutina de la matriz (si no lo hizo el prompt 1).

### 2C · Si entra Gemini

- **Gemini CLI** (en tu Mac, con terminal): lee `GEMINI.md`, valida y publica con los frenos de git
  (`sh ia/instalar.sh`). Para correr solo cada día necesita un programador en tu computadora; sin él
  trabaja cuando se lo pidas.
- **Gemini en la web (Gems o acciones programadas):** pega `ia/INSTRUCCIONES_PROYECTO.md` en el Gem.
  Si no puede escribir en GitHub, prepara el cierre como «Registro pendiente para el repositorio».

Sin escritura en GitHub y sin programador, Gemini no puede ser el ejecutor diario; puede ayudar
cuando se lo pidas.

### Prompt 3 · Verificar el cambio (en la IA entrante)

```
Vas a hacer el cierre diario de la matriz Castorena (lianfixx/Cerebro-Castorena-, rama main). Lee AGENTS.md, ia/REGLAS.md, cerebro/CAMBIAR_DE_IA.md y cerebro/skill/SKILL.md con operacion.md, y cúmplelos. No envíes correos.

1. Comprueba en cerebro/ESTADO.json que la IA saliente registró su pausa y que executor_current está en null.
2. Comprueba tus capacidades reales: lectura y escritura en lianfixx/Cerebro-Castorena-, lectura de lianfixx/INDEP, Google Drive y tu programador de tareas. Dime cuáles tienes y cuáles no.
3. Si tienes escritura en GitHub y programador, pon executor_current con tu id y registra tu tarea en ESTADO.json (nombre, ID real, horario, conectores y fecha de comprobación). Si te falta algo, no te actives: regístralo y dime qué hacer.
4. Valida con `python3 cerebro/skill/scripts/validar_matriz.py cerebro`, haz un commit con la línea «Agente:» y el trailer «IA-Actor:», comprueba el SHA esperado y nunca uses force. Dame el resumen y el commit.
```
