# Diccionario de Datos / Data Dictionary

## Dataset: Indicadores de Mortalidad y Morbilidad por Municipio

**Fuente / Source:** Ministerio de Salud y Proteccion Social - datos.gov.co
**URL:** https://www.datos.gov.co/Salud-y-Protecci-n-Social/Indicadores-mortalidad-y-morbilidad-seg-n-departam/4e4i-ua65
**Periodo / Period:** 2005 - 2020
**Granularidad / Granularity:** Un registro por municipio por ano / One record per municipality per year
**Registros esperados / Expected rows:** 512 (sin duplicados / without duplicates)

---

## Columnas / Columns

| Columna | Descripcion (ES) | Description (EN) | Tipo esperado | Rango esperado |
|---------|-------------------|-------------------|---------------|----------------|
| `cod_departamento` | Codigo DIVIPOLA del departamento | DIVIPOLA department code | int64 | 5 - 99 |
| `departamento` | Nombre del departamento | Department name | string | 22 departamentos unicos / 22 unique departments |
| `cod_municipio` | Codigo DIVIPOLA del municipio | DIVIPOLA municipality code | int64 | 5001 - 99001 |
| `municipio` | Nombre del municipio | Municipality name | string | 32 municipios unicos / 32 unique municipalities |
| `ano` | Ano del reporte | Reporting year | int64 | 2005 - 2020 |
| `bajo_peso_nacer` | Porcentaje de nacidos vivos con bajo peso | % of live births with low weight | float64 | 0 - 100 |
| `controles_prenatales` | Promedio de controles prenatales | Average prenatal checkups | float64 | 0 - 15 |
| `fecundidad_adolescente` | Tasa de fecundidad en mujeres 15-19 anos | Teen fertility rate (15-19 years) | float64 | 0 - 200 |
| `mortalidad_fetal` | Tasa de mortalidad fetal | Fetal mortality rate | float64 | 0 - 200 |
| `mortalidad_general` | Tasa de mortalidad general | General mortality rate | float64 | 0 - 20 |
| `mortalidad_infantil` | Tasa de mortalidad infantil (<1 ano) | Infant mortality rate (<1 year) | float64 | 0 - 100 |
| `mortalidad_materna` | Razon de mortalidad materna por 100,000 | Maternal mortality ratio per 100K | float64 | 0 - 500 |
| `mortalidad_neonatal` | Tasa de mortalidad neonatal | Neonatal mortality rate | float64 | 0 - 50 |
| `partos_cesarea` | Porcentaje de partos por cesarea | % cesarean deliveries | float64 | 0 - 100 |
| `partos_institucionales` | Porcentaje de partos institucionales | % institutional deliveries | float64 | 0 - 100 |

---

## Problemas de Calidad Conocidos (Version Sucia) / Known Quality Issues (Dirty Version)

1. **Valores faltantes / Missing values:** Varias columnas de indicadores tienen valores nulos, asi como la columna `departamento`. Some indicator columns and the `departamento` column contain null values.
2. **Ano como float / Year as float:** La columna `ano` esta almacenada como float (e.g., 2015.0) en lugar de int. The `ano` column is stored as float instead of int.
3. **Codigo municipio con formato incorrecto / Municipality code with bad format:** La columna `cod_municipio` contiene comas (e.g., "5,001") y valores "sin dato". The `cod_municipio` column has commas and "sin dato" entries.
4. **Inconsistencias en texto / Text inconsistencies:** La columna `departamento` tiene problemas de mayusculas/minusculas y espacios en blanco. The `departamento` column has case and whitespace inconsistencies.
5. **Valores invalidos / Invalid values:** Algunas columnas de porcentaje tienen valores menores a 0 o mayores a 100. Some percentage columns have values below 0 or above 100.

---

## Notas / Notes

- **Mortalidad general** (general mortality): Tasa de defunciones por cada 1,000 habitantes. Number of deaths per 1,000 population.
- **Mortalidad infantil** (infant mortality): Defunciones de menores de 1 ano por cada 1,000 nacidos vivos. Deaths of children under 1 year per 1,000 live births.
- **Mortalidad neonatal** (neonatal mortality): Defunciones en los primeros 28 dias de vida por cada 1,000 nacidos vivos. Deaths in the first 28 days of life per 1,000 live births.
- **Mortalidad fetal** (fetal mortality): Defunciones fetales por cada 1,000 nacimientos (vivos y muertos). Fetal deaths per 1,000 births (live and still).
- **Mortalidad materna** (maternal mortality): Defunciones maternas por cada 100,000 nacidos vivos. Maternal deaths per 100,000 live births.
- **Bajo peso al nacer** (low birth weight): Porcentaje de nacidos vivos con peso inferior a 2,500 gramos. Percentage of live births weighing less than 2,500 grams.
- **Partos institucionales** (institutional deliveries): Porcentaje de partos atendidos en instituciones de salud. Percentage of deliveries attended in health institutions.
- **Partos cesarea** (cesarean deliveries): Porcentaje de partos realizados por cesarea. Percentage of deliveries performed by cesarean section.
- **Fecundidad adolescente** (teen fertility): Numero de nacimientos por cada 1,000 mujeres entre 15 y 19 anos. Number of births per 1,000 women aged 15-19.
- **Controles prenatales** (prenatal checkups): Promedio de visitas de control prenatal por embarazo. Average number of prenatal care visits per pregnancy.

## Municipios / Municipalities

El dataset incluye 32 municipios de 22 departamentos de Colombia. Los datos cubren capitales departamentales y municipios representativos. / The dataset includes 32 municipalities from 22 Colombian departments. Data covers departmental capitals and representative municipalities.
