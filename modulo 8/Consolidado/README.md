# 👶 Módulo 8 – Redes Neuronales y Predicción de la Tasa de Natalidad

Este proyecto corresponde al **Módulo 8 del Bootcamp de Ciencia de Datos**.  
El objetivo fue aplicar **redes neuronales artificiales (ANN)** para modelar la **tasa de natalidad en distintos países**, a partir de variables socioeconómicas y demográficas, evaluando distintas arquitecturas, funciones de activación, regularización y optimizadores.

---

## 🎯 Objetivos

1. Diseñar y entrenar una red neuronal para resolver un problema de regresión.  
2. Aplicar conocimientos sobre funciones de activación, optimizadores y estrategias para prevenir sobreajuste.  
3. Evaluar y comparar los resultados obtenidos con diferentes configuraciones de la red.  
4. Analizar la influencia de cada variable en la predicción y extraer conclusiones sobre patrones socioeconómicos globales.  

---

## 📂 Contenido
- `modulo8_modelo.py`: Script en Python con el código de entrenamiento, pruebas y comparaciones.  
- `graficos/`: Carpeta con heatmaps de correlación, curvas de pérdida y comparaciones de métricas.  

---

## 🛠️ Tecnologías usadas
- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  
- TensorFlow / Keras para el diseño y entrenamiento de redes neuronales  
- Callbacks de entrenamiento (**EarlyStopping**)  
- Regularización con **Dropout y L2**  

---

## 📋 Requerimientos implementados

1. **📊 Carga y exploración de datos (1 punto)**  
   - Carga del dataset con variables socioeconómicas.  
   - Análisis descriptivo, detección de nulos y correlaciones.  
   - Visualización mediante **heatmap**.  

2. **🧠 Diseño y entrenamiento del modelo (5 puntos)**  
   - Red neuronal con capas densas y activaciones `relu` y `tanh`.  
   - Evaluación de distintos optimizadores (`Adam`, `SGD`).  
   - Aplicación de regularización: **Dropout** y **L2**.  
   - Comparación de configuraciones con métricas de pérdida en validación.  

3. **⚙️ Evaluación y optimización del modelo (3 puntos)**  
   - Métricas de evaluación: **MSE, MAE y R²**.  
   - Comparación de resultados en datos de prueba.  
   - Predicciones vs. valores reales.  

4. **📑 Análisis de resultados y reflexión final (1 punto)**  
   - Identificación de variables influyentes en la natalidad.  
   - Relación de hallazgos con tendencias demográficas globales.  
   - Propuestas de mejora para optimización futura.  

---

## 📊 Visualizaciones
- 🔹 Heatmap de correlación entre variables socioeconómicas.  
- 🔹 Curvas de pérdida (entrenamiento vs. validación) para distintas configuraciones.  
- 🔹 Tabla comparativa de configuraciones de la red neuronal.  

---

## 📝 Reflexión Final

El análisis de resultados muestra que las variables más influyentes en la predicción de la natalidad son el **PIB per cápita** (correlación negativa de -0.86), la **edad promedio de maternidad** (r = -0.30), la **tasa de empleo femenino** (r = 0.24) y la **urbanización** (r = 0.20), lo que confirma la importancia de los factores económicos y sociales en la dinámica demográfica.  

En términos de desempeño, con 50 épocas de entrenamiento el modelo base presentó un error elevado (MSE = 369.9 y R² = -4.14), pero al extenderlo a 150 épocas mejoró de manera significativa (MSE = 34.7, MAE = 5.1 y R² = 0.51), alcanzando un nivel de ajuste razonable en un dataset relativamente pequeño. La configuración más consistente fue la combinación **ReLU + Adam + MAE**.  

De cara a futuras optimizaciones, explorar un ajuste más fino de los hiperparámetros podría ayudar a mejorar el coeficiente de determinación, idealmente acercándolo a valores superiores a 0.9, aunque siempre considerando estrategias de regularización, como incrementar la tasa de **Dropout por capa**, para evitar el sobreajuste.  

Estos hallazgos son coherentes con las **tendencias demográficas globales**, en las que el desarrollo económico, la educación y el acceso a servicios de salud tienden a reducir la natalidad, mientras que factores como el empleo femenino y la urbanización contribuyen a transformaciones en los patrones reproductivos.  

---

✍️ *Autor: Liroy Cataldo*

