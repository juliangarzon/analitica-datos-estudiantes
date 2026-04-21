# Semana 11 Workshop: Dashboards Interactivos con Plotly + Streamlit

**Duración sugerida**: 2 horas

## Propósito

En esta sesión no vamos a construir una aplicación desde cero frente al tablero. Primero verás una app terminada, luego seguirás una guía paso a paso con una plantilla funcional y, al final, adaptarás esa base a un dataset de tu elección.

## Dataset guiado

Usaremos el archivo local:

- `../data/calidad_aire_risaralda.csv`

Este dataset permite construir un dashboard claro porque tiene:

- fechas
- municipios
- estaciones
- tipo de material particulado (`PM10` y `PM2.5`)
- mediciones numéricas

## Flujo del workshop

| Momento | Objetivo | Entregable |
|--------|----------|------------|
| Demo | Entender cómo luce una app útil | Checklist de componentes |
| Guía paso a paso | Completar una app base | `streamlit_app_starter.py` funcionando |
| Extensión | Adaptar la plantilla | Propuesta propia con otro dataset |

## Archivos

| Archivo | Uso |
|--------|-----|
| `workshop_starter.ipynb` | Práctica guiada de Plotly con el dataset de calidad del aire |
| `workshop_solution.ipynb` | Solución del notebook guiado |
| `streamlit_app_starter.py` | Plantilla incompleta del dashboard |
| `streamlit_app_solution.py` | Solución completa del dashboard |
| `streamlit_demo_violencia.py` | Demo terminada para mostrar al inicio de la clase |

## Parte 1. Mira la demo antes de escribir código

Abre la demo del profesor:

```bash
streamlit run streamlit_demo_violencia.py
```

Mientras la observas, identifica:

1. Qué filtros tiene.
2. Qué métricas resume.
3. Qué preguntas permite responder.
4. Qué decisiones de diseño ayudan a leer mejor los datos.

## Parte 2. Completa la app guiada

Abre la plantilla:

```bash
streamlit run streamlit_app_starter.py
```

Debes completar los `TODO` para que la app tenga:

1. Título y descripción.
2. Filtros en la barra lateral.
3. Tres métricas principales.
4. Tres visualizaciones interactivas.
5. Una tabla opcional con datos filtrados.

## Parte 3. Pásala de plantilla a producto útil

Cuando la app base funcione, agrega al menos **una** mejora:

- un filtro adicional
- una pestaña nueva
- un gráfico distinto
- una conclusión escrita en lenguaje natural
- un botón de descarga del subconjunto filtrado

## Parte 4. Adáptala a otro dataset

En equipos, escoge un dataset público que tenga al menos:

- una variable temporal
- una o más variables categóricas
- una métrica numérica

Tu reto es reutilizar la plantilla y construir una mini app que responda una pregunta clara.

### Preguntas guía

- ¿Qué está cambiando en el tiempo?
- ¿Qué categorías tienen el valor más alto o más bajo?
- ¿Qué filtros serían útiles para un usuario real?
- ¿Qué insight debería entender alguien en menos de 30 segundos?

## Criterios mínimos de entrega

| Criterio | Esperado |
|----------|----------|
| Funciona | La app corre sin errores |
| Filtros | Al menos 3 filtros útiles |
| Métricas | Al menos 3 KPIs |
| Gráficos | Al menos 3 gráficos interactivos |
| Claridad | La app comunica una pregunta o propósito |

## Comandos útiles

Instalar dependencias:

```bash
pip install streamlit plotly pandas
```

Ejecutar la plantilla:

```bash
streamlit run streamlit_app_starter.py
```

Ejecutar la solución:

```bash
streamlit run streamlit_app_solution.py
```

## Cierre esperado

Al final del workshop deberías tener:

1. Una app guiada funcionando con el dataset de calidad del aire.
2. Una lista de cambios para adaptarla a otro dataset.
3. Un primer prototipo propio listo para mostrar.
