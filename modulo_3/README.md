# 🌍 Módulo 3 – Análisis de Datos de Migración

Este proyecto corresponde al **Módulo 3 del Bootcamp de Ciencia de Datos**.  
El objetivo fue aplicar técnicas de **limpieza, transformación y análisis de datos** con **NumPy y Pandas**, utilizando un dataset de migración internacional.

## 📂 Contenido
- `migracion.csv`: Dataset original entregado.  
- `consolidado_modulo3.py`: Script en Python con el análisis.  
- `Migracion_Limpio.csv`: Dataset limpio y exportado tras la depuración.  

## 🛠️ Tecnologías usadas
- Python (Pandas, NumPy)  
- Jupyter Notebook / Google Colab  

## 📋 Requerimientos implementados
1. **Limpieza y transformación de datos**  
   - Identificación de valores nulos y duplicados.  
   - Detección y filtrado de *outliers* mediante IQR.  
   - Estandarización de categorías en la columna `Razon_Migracion`.  

2. **Análisis exploratorio (EDA)**  
   - Obtención de estadísticas descriptivas.  
   - Cálculo de media, mediana y conteos por categorías.  
   - Análisis de PIB e IDH de países de origen y destino.  

3. **Agrupamiento y sumarización**  
   - Suma de migrantes por razón de migración.  
   - Media del IDH por país de origen.  
   - Ordenamiento por cantidad de migrantes.  

4. **Filtros y selección de datos**  
   - Migraciones por conflicto.  
   - Países con IDH destino > 0.90.  
   - Creación de la columna `Diferencia_IDH`.  

5. **Exportación de datos**  
   - Generación de archivo `Migracion_Limpio.csv` con los datos finales.  

## 🎯 Resultados principales
- No se detectaron valores nulos ni duplicados.  
- Se identificó y eliminó un *outlier* en los datos de migración.  
- Se realizó un mapeo de razones de migración para mayor claridad (`Económica → Trabajo`, `Conflicto → Guerra`).  
- Se calcularon indicadores como media, mediana y PIB promedio.  
- Se obtuvo la distribución de migrantes por razones (económica, conflicto, educativa).  

## 📊 Visualizaciones
Algunos de los resultados esperados del análisis incluyen:  

![Distribución de migrantes](img/migracion_distribucion.png)  
![Boxplot para outliers](img/migracion_outliers.png)  
![Comparación de IDH](img/migracion_idh.png)  

---

✍️ *Autor: Liroy Cataldo*
