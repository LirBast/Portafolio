# 🏅 Módulo 4 – Análisis de Datos de Atletas Olímpicos

Este proyecto corresponde al **Módulo 4 del Bootcamp de Ciencia de Datos**.  
El objetivo fue **analizar patrones de rendimiento deportivo**, identificar factores que influyen en el éxito de los atletas y realizar predicciones simples a partir de sus características.

## 📂 Contenido
- `olimpicos.csv`: Dataset original con información de los atletas.  
- `consolidado_modulo4.py`: Script en Python con todo el análisis.  
- `graficos/`: Carpeta con las visualizaciones generadas (histogramas, boxplots, heatmaps, regresión).  

## 🛠️ Tecnologías usadas
- Python (Pandas, NumPy, SciPy, Scikit-learn)  
- Seaborn y Matplotlib para visualización  
- Jupyter Notebook / Google Colab  

## 📋 Requerimientos implementados
1. **🔍 Análisis Exploratorio de Datos**  
   - Carga y revisión de dataset (`.head()`, `.info()`, `.describe()`).  
   - Histograma del número de entrenamientos semanales.  

2. **📊 Estadística Descriptiva**  
   - Identificación de tipo de variable en cada columna.  
   - Media, mediana y moda de medallas obtenidas.  
   - Desviación estándar de altura de atletas.  
   - Detección de valores atípicos en el peso con IQR y boxplot.  

3. **📈 Análisis de Correlación**  
   - Correlación de Pearson entre entrenamientos semanales y medallas totales.  
   - Gráfico de dispersión: Peso vs Medallas.  
   - Interpretación de significancia estadística.  

4. **📉 Regresión Lineal**  
   - Modelo para predecir medallas en función de entrenamientos semanales.  
   - Obtención de coeficientes (pendiente e intercepto).  
   - Cálculo del R² y análisis del ajuste del modelo.  
   - Gráfico de regresión con `seaborn.regplot()`.  

5. **🎨 Visualización de Datos**  
   - Heatmap de correlaciones entre variables numéricas.  
   - Boxplot de medallas por disciplina deportiva.  
   - Personalización de gráficos con títulos, etiquetas y colores.  

## 🎯 Resultados principales
- Se observaron distribuciones realistas en entrenamientos, altura y peso de atletas.  
- La relación entre entrenamientos semanales y medallas fue positiva, pero estadísticamente no significativa (Pearson = 0.57, p = 0.18).  
- El modelo de regresión lineal explicó un **32% de la varianza (R² = 0.32)**, lo que indica que existen otros factores importantes además del entrenamiento.  
- No se detectaron *outliers* relevantes en la variable peso.  
- Se identificaron patrones de medallas en distintas disciplinas deportivas.  

## 📊 Visualizaciones
Algunas de las visualizaciones generadas en este módulo:  

![Figura 1](modulo_4/imagenes/Figure_1.png)
![Figura 2](modulo_4/imagenes/Figure_2.png)
![Figura 3](modulo_4/imagenes/Figure_3.png)
![Figura 4](modulo_4/imagenes/Figure_4.png)
![Figura 5](modulo_4/imagenes/Figure_5.png)
![Figura 6](modulo_4/imagenes/Figure_6.png)

---

✍️ *Autor: Liroy Cataldo*

