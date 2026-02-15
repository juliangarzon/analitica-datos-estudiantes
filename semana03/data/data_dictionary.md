# Diccionario de Datos / Data Dictionary

## Dataset: Estadisticas en Educacion en Preescolar, Basica y Media

**Fuente / Source:** Ministerio de Educacion Nacional (MEN) - datos.gov.co
**Periodo / Period:** 2011 - 2024
**Granularidad / Granularity:** Un registro por departamento por ano
**Registros esperados / Expected rows:** 462 (sin duplicados)

---

## Columnas / Columns

| Columna | Descripcion (ES) | Description (EN) | Tipo esperado | Rango esperado |
|---------|-------------------|-------------------|---------------|----------------|
| `ano` | Ano del reporte | Reporting year | int64 | 2011 - 2024 |
| `c_digo_departamento` | Codigo DANE del departamento | DANE department code | int64 | 5 - 99 |
| `departamento` | Nombre del departamento | Department name | string | 34 departamentos unicos |
| `poblacion_5_16` | Poblacion entre 5 y 16 anos | Population aged 5-16 | int64 | > 0 |
| `tasa_matriculacion_5_16` | Tasa de matriculacion (5-16 anos) | Enrollment rate (5-16) | float64 | 0 - 100 |
| `cobertura_neta` | Cobertura neta total | Net coverage (total) | float64 | 0 - 100 |
| `cobertura_neta_transicion` | Cobertura neta en transicion | Net coverage (transition/preschool) | float64 | 0 - 100 |
| `cobertura_neta_primaria` | Cobertura neta en primaria | Net coverage (primary) | float64 | 0 - 100 |
| `cobertura_neta_secundaria` | Cobertura neta en secundaria | Net coverage (secondary) | float64 | 0 - 100 |
| `cobertura_neta_media` | Cobertura neta en media | Net coverage (high school) | float64 | 0 - 100 |
| `cobertura_bruta` | Cobertura bruta total | Gross coverage (total) | float64 | 0 - 200+ |
| `cobertura_bruta_transicion` | Cobertura bruta en transicion | Gross coverage (transition) | float64 | 0 - 200+ |
| `cobertura_bruta_primaria` | Cobertura bruta en primaria | Gross coverage (primary) | float64 | 0 - 200+ |
| `cobertura_bruta_secundaria` | Cobertura bruta en secundaria | Gross coverage (secondary) | float64 | 0 - 200+ |
| `cobertura_bruta_media` | Cobertura bruta en media | Gross coverage (high school) | float64 | 0 - 200+ |
| `tamano_promedio_grupo` | Tamano promedio del grupo | Average class size | float64 | > 0 |
| `sedes_conectadas_a_internet` | % de sedes con internet | % of schools with internet | float64 | 0 - 100 |
| `desercion` | Tasa de desercion total | Total dropout rate | float64 | 0 - 100 |
| `desercion_transicion` | Desercion en transicion | Dropout rate (transition) | float64 | 0 - 100 |
| `desercion_primaria` | Desercion en primaria | Dropout rate (primary) | float64 | 0 - 100 |
| `desercion_secundaria` | Desercion en secundaria | Dropout rate (secondary) | float64 | 0 - 100 |
| `desercion_media` | Desercion en media | Dropout rate (high school) | float64 | 0 - 100 |
| `aprobacion` | Tasa de aprobacion total | Total approval rate | float64 | 0 - 100 |
| `aprobacion_transicion` | Aprobacion en transicion | Approval rate (transition) | float64 | 0 - 100 |
| `aprobacion_primaria` | Aprobacion en primaria | Approval rate (primary) | float64 | 0 - 100 |
| `aprobacion_secundaria` | Aprobacion en secundaria | Approval rate (secondary) | float64 | 0 - 100 |
| `aprobacion_media` | Aprobacion en media | Approval rate (high school) | float64 | 0 - 100 |
| `reprobacion` | Tasa de reprobacion total | Total failure rate | float64 | 0 - 100 |
| `reprobacion_transicion` | Reprobacion en transicion | Failure rate (transition) | float64 | 0 - 100 |
| `reprobacion_primaria` | Reprobacion en primaria | Failure rate (primary) | float64 | 0 - 100 |
| `reprobacion_secundaria` | Reprobacion en secundaria | Failure rate (secondary) | float64 | 0 - 100 |
| `reprobacion_media` | Reprobacion en media | Failure rate (high school) | float64 | 0 - 100 |
| `repitencia` | Tasa de repitencia total | Total repetition rate | float64 | 0 - 100 |
| `repitencia_transicion` | Repitencia en transicion | Repetition rate (transition) | float64 | 0 - 100 |
| `repitencia_primaria` | Repitencia en primaria | Repetition rate (primary) | float64 | 0 - 100 |
| `repitencia_secundaria` | Repitencia en secundaria | Repetition rate (secondary) | float64 | 0 - 100 |
| `repitencia_media` | Repitencia en media | Repetition rate (high school) | float64 | 0 - 100 |

---

## Notas / Notes

- **Cobertura neta** (net coverage): Porcentaje de la poblacion en edad correspondiente que esta matriculada en el nivel educativo apropiado. No puede superar 100%.
- **Cobertura bruta** (gross coverage): Incluye estudiantes de cualquier edad en el nivel educativo. Puede superar 100% si hay estudiantes en extra-edad.
- **Desercion** (dropout): Porcentaje de estudiantes que abandonan el sistema educativo durante el ano escolar.
- **Aprobacion** (approval): Porcentaje de estudiantes que aprueban el ano escolar.
- **Reprobacion** (failure): Porcentaje de estudiantes que reprueban el ano escolar.
- **Repitencia** (repetition): Porcentaje de estudiantes que repiten el ano escolar.
- Las columnas `tamano_promedio_grupo` y `sedes_conectadas_a_internet` solo estan disponibles hasta 2017.

## Departamentos de Colombia

El dataset incluye los 32 departamentos de Colombia, mas Bogota D.C. y un registro nacional. Ejemplos: Antioquia, Atlantico, Bogota D.C., Bolivar, Boyaca, Caldas, Caqueta, Cauca, Cesar, Cordoba, Cundinamarca, Choco, Huila, La Guajira, Magdalena, Meta, Narino, Norte de Santander, Quindio, Risaralda, Santander, Sucre, Tolima, Valle del Cauca, Arauca, Casanare, Putumayo, San Andres, Amazonas, Guainia, Guaviare, Vaupes, Vichada.
