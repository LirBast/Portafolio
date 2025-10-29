# 🌍 Módulo 9 – Análisis de Movimientos Migratorios con Spark

Este proyecto corresponde al **Módulo 9 del Bootcamp de Ciencia de Datos**.  
El objetivo fue aplicar conceptos de **Big Data con Apache Spark y PySpark** para analizar patrones de migración humana, utilizando RDDs, DataFrames, Spark SQL y MLlib para predicción de flujos migratorios.

---

## 📘 Enunciado

**EVALUACIÓN FINAL: ANÁLISIS DE MOVIMIENTOS MIGRATORIOS CON SPARK**  

Eres parte de un equipo de analistas de datos encargado de estudiar las tendencias de migración humana en el siglo XXI utilizando Big Data. Para ello, trabajarás con un conjunto de datos que contiene información sobre migraciones entre distintos países, sus causas y el impacto socioeconómico en las regiones de origen y destino.  

**Objetivos de la actividad:**
1. Aplicar conceptos de Big Data utilizando Apache Spark y PySpark.  
2. Explorar y transformar datos con RDDs y DataFrames.  
3. Realizar consultas con Spark SQL.  
4. Implementar modelos de aprendizaje automático con MLlib.  

---

## 📂 Contenido
- `modulo9_migracion.ipynb`: Notebook en Google Colab con el código completo.  
- `migraciones.csv`: Dataset de movimientos migratorios.  
- `resultado_pib.parquet`: Archivo generado en formato **Parquet** con agregaciones de PIB.  

---

## 🛠️ Tecnologías usadas
- Python + Google Colab
 
- **Apache Spark / PySpark** (RDDs, DataFrames, Spark SQL, MLlib)  
- Machine Learning con **Logistic Regression** en MLlib  

---

## 📋 Requerimientos implementados

1. **📊 Carga y exploración de datos **  
   - Carga del dataset con información migratoria.  
   - Conversión a **RDD y DataFrame**.  
   - Exploración: primeras filas, esquema y estadísticas descriptivas.  

2. **⚙️ Procesamiento de datos con RDDs y DataFrames **  
   - Transformaciones en RDDs: `filter`, `map`, `flatMap`.  
   - Acciones en RDDs: `take`, `count`, `collect`.  
   - Operaciones en DataFrames: filtrado, agregaciones y ordenamiento.  
   - Exportación de resultados en **formato Parquet**.  

3. **🗂️ Consultas con Spark SQL **  
   - Registro del DataFrame como **tabla temporal**.  
   - Consultas de los principales países de origen y destino.  
   - Análisis de las principales **razones de migración por región**.  

4. **🤖 Aplicación de MLlib para predicción **  
   - Conversión de datos en vectores de características (`VectorAssembler`).  
   - Entrenamiento de un modelo de **Regresión Logística**.  
   - Evaluación de precisión del modelo.  

---

## 📊 Resultados principales
- RDDs permitieron un manejo flexible de transformaciones (ej. filtrar migraciones económicas).  
- DataFrames y Spark SQL facilitaron consultas complejas, como identificar los principales destinos o las razones más comunes de migración.  
- Se guardaron resultados de agregaciones en formato Parquet para optimizar el almacenamiento.  
- El modelo de **regresión logística** en MLlib logró ejecutarse, pero debido al tamaño muy reducido del dataset (solo 5 registros), la precisión fue **0**, ya que el conjunto de prueba quedó con un solo dato.  

---

## 📝 Reflexión Final

Este módulo permitió integrar el uso de **Big Data con Apache Spark**, explorando cómo trabajar con RDDs, DataFrames y Spark SQL en un flujo completo de análisis. Las transformaciones con RDDs fueron útiles para entender la estructura de los datos en bajo nivel, mientras que los DataFrames y consultas SQL ofrecieron mayor expresividad y eficiencia para agregaciones y análisis exploratorio. La exportación en Parquet reflejó la importancia de usar formatos optimizados en entornos Big Data.  

En cuanto al modelado predictivo, la regresión logística en MLlib mostró el procedimiento de preparación de datos, entrenamiento y evaluación. Sin embargo, el tamaño extremadamente reducido del dataset no permitió obtener métricas representativas, lo que evidencia la necesidad de **grandes volúmenes de datos** para que Spark muestre todo su potencial.  

En síntesis, este módulo fue un acercamiento valioso a la **analítica de datos a gran escala**, reforzando la importancia del contexto Big Data y el uso de Spark como herramienta central para el procesamiento y análisis de información compleja.  

---

✍️ *Autor: Liroy Cataldo*

