# Workshop: Financial Statements Analysis with Pandas

## Taller Semana 2: Analisis de Estados Financieros con Pandas

---

## Overview / Descripcion General

In this workshop, you will analyze a real dataset of financial statements from the Colombian government's open data portal (datos.gov.co). You will practice loading, exploring, filtering, and summarizing data using pandas.

En este taller, analizaras un dataset real de estados financieros del portal de datos abiertos del gobierno colombiano (datos.gov.co). Practicaras cargar, explorar, filtrar y resumir datos usando pandas.

---

## Objectives / Objetivos

By the end of this workshop, you will be able to:

1. Load CSV data from a URL using pandas
2. Explore data structure with `head()`, `info()`, `describe()`, and `shape`
3. Identify and count unique values in categorical columns
4. Filter data using boolean conditions
5. Aggregate data using `groupby()` and summary functions
6. Answer business questions with data
7. Create a basic visualization

Al finalizar este taller, seras capaz de:

1. Cargar datos CSV desde una URL usando pandas
2. Explorar la estructura de datos con `head()`, `info()`, `describe()`, y `shape`
3. Identificar y contar valores unicos en columnas categoricas
4. Filtrar datos usando condiciones booleanas
5. Agregar datos usando `groupby()` y funciones de resumen
6. Responder preguntas de negocio con datos
7. Crear una visualizacion basica

---

## Dataset Information / Informacion del Dataset

| Field | Value |
|-------|-------|
| **Name** | Estados Financieros (Financial Statements) |
| **Source** | datos.gov.co |
| **Records** | ~1,665 rows |
| **Format** | CSV |

### Expected Columns / Columnas Esperadas

The dataset contains financial statement information with columns such as:
- Entity information (name, NIT/tax ID)
- Account classifications (categories, subcategories)
- Monetary values
- Time period information

---

## Tasks / Tareas

Complete all tasks in the provided starter notebook (`workshop_starter.ipynb`).

### Task 1: Load and Explore (Cargar y Explorar)

1. Import pandas
2. Load the dataset from the URL
3. Display the shape (rows, columns)
4. Show the first 10 rows
5. Display data types with `info()`
6. Show summary statistics with `describe()`

### Task 2: Data Quality Check (Verificacion de Calidad)

1. Check for missing values in each column
2. Identify the data type of each column
3. Find any columns that might need type conversion

### Task 3: Categorical Analysis (Analisis Categorico)

1. List all unique categories in the main category column
2. Count how many records are in each category
3. Identify the category with the most records

### Task 4: Numerical Analysis (Analisis Numerico)

1. Calculate the total value across all records
2. Find the minimum and maximum values
3. Calculate the mean and median values
4. Identify the top 10 records by value

### Task 5: Filtering (Filtrado)

1. Filter records where value is greater than 1 billion (1,000,000,000)
2. Filter records for a specific category of your choice
3. Combine both filters (value > 1 billion AND specific category)

### Task 6: Grouping (Agrupacion)

1. Group by category and calculate total value per category
2. Sort the results from highest to lowest
3. Display the top 5 categories by total value

### Task 7: Visualization (Visualizacion)

Create a bar chart showing the top 10 categories by total value.

---

## Deliverables / Entregables

Submit a completed Jupyter notebook (`.ipynb`) that includes:

1. **All code executed** - All cells should show output
2. **Answers to questions** - Use markdown cells to write your answers/observations
3. **At least one visualization** - A bar chart as requested in Task 7
4. **Your name and date** - In the first cell of the notebook

---

## Grading Criteria / Criterios de Evaluacion

| Criteria | Points |
|----------|--------|
| Data loading and exploration complete | 20 |
| Data quality check complete | 15 |
| Categorical analysis correct | 15 |
| Numerical analysis correct | 15 |
| Filtering correct | 15 |
| Grouping correct | 15 |
| Visualization included | 5 |
| **Total** | **100** |

### Grading Notes / Notas de Evaluacion

- **Full credit:** Code works correctly and includes brief explanations
- **Partial credit:** Code has minor errors but shows understanding
- **No credit:** Code missing or does not demonstrate understanding

---

## Submission / Entrega

- **Format:** Jupyter Notebook (.ipynb)
- **Filename:** `workshop_semana02_APELLIDO.ipynb`
- **Submit to:** Course GitHub repository
- **Deadline:** Before next class (Semana 3)

---

## Resources / Recursos

### Documentation

- [pandas documentation](https://pandas.pydata.org/docs/)
- [pandas cheat sheet (PDF)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

### Video Tutorials

- [Corey Schafer - Pandas Tutorial](https://www.youtube.com/watch?v=ZyhVh-qRZPA)

### Dataset Source

- [datos.gov.co - Estados Financieros](https://www.datos.gov.co/browse?q=estados%20financieros)

---

## Tips / Consejos

1. **Run cells in order** - Variables defined in earlier cells are used in later cells
2. **Restart kernel if stuck** - Kernel > Restart & Run All
3. **Use tab completion** - Type `df.` and press Tab to see available methods
4. **Read error messages** - Python error messages tell you the line number and type of error
5. **Google is your friend** - Search "pandas how to..." for quick answers

---

## Common Errors / Errores Comunes

| Error | Cause | Solution |
|-------|-------|----------|
| `KeyError: 'column_name'` | Column name spelled wrong | Check exact column names with `df.columns` |
| `TypeError: '>' not supported` | Comparing wrong data types | Check column dtype with `df['col'].dtype` |
| `ModuleNotFoundError` | pandas not installed | Run `pip install pandas` |
| `FileNotFoundError` | Wrong file path | Use the provided URL instead |

---

Good luck! / Buena suerte!
