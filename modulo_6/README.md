# 🌱 Módulo 6 – Análisis del Impacto del Cambio Climático en la Producción Agrícola

Este proyecto corresponde al **Módulo 6 del Bootcamp de Ciencia de Datos**.  
El objetivo fue **evaluar cómo los factores climáticos afectan la producción agrícola en distintos países**, aplicando técnicas de **regresión y clasificación supervisada**, junto con **optimización de modelos** y análisis de resultados.

## 📂 Contenido
- `cambio_climatico_agricultura.py`: Script en Python con el análisis completo.  
- `graficos/`: Carpeta con curvas ROC y comparaciones de modelos.  

## 🛠️ Tecnologías usadas
- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  
- Modelos de regresión y clasificación  
- Optimización de hiperparámetros con GridSearchCV  

## 📋 Requerimientos implementados
1. **📊 Carga y Exploración de Datos**  
   - Dataset con variables de clima y producción agrícola.  
   - Análisis de nulos, tipos de datos y descripción estadística.  

2. **⚙️ Preprocesamiento y Escalamiento**  
   - One-Hot Encoding para variables categóricas (País).  
   - Normalización de variables numéricas con `StandardScaler`.  
   - División en conjunto de entrenamiento (80%) y prueba (20%).  

3. **🤖 Modelos de Aprendizaje Supervisado**  
   - **Regresión:**  
     - Regresión lineal y polinómica.  
     - Árboles de decisión y Random Forest.  
     - Métricas: MAE, MSE, R².  
   - **Clasificación:**  
     - Variable categórica **Impacto** (Bajo, Medio, Alto).  
     - Modelos: KNN, Árbol de Decisión, SVM.  
     - Métricas: Accuracy, Precisión, Recall, F1-Score.  
     - Curvas ROC-AUC para clases multiclase.  

4. **🔧 Optimización de Modelos**  
   - **Random Forest:** ajuste de `max_depth`, `min_samples_split` y `n_estimators`.  
   - **SVM:** ajuste de `C`, `gamma` y `kernel`.  
   - Regularización con **Ridge** y **Lasso**.  

5. **📈 Análisis de Resultados y Conclusiones**  
   - Comparación de desempeño entre modelos lineales, polinómicos y basados en árboles.  
   - Evaluación de clasificadores según métricas y curvas ROC.  

## 🎯 Resultados principales
- **Regresiones lineales y polinómicas:** R² bajo o negativo → modelos poco adecuados.  
- **Random Forest y Árboles de Decisión:** mejores resultados de predicción (capturan interacciones).  
- **Clasificación:**  
  - KNN y Árbol de Decisión → Accuracy ≈ 0.80 y F1 ≈ 0.82.  
  - SVM → Accuracy ≈ 0.60 y F1 ≈ 0.45 (mejoró a ≈ 0.66 tras GridSearchCV).  

## 📊 Visualizaciones
Algunas de las visualizaciones generadas en este módulo:  

- 🔹 **Curvas ROC** para clases Bajo, Medio y Alto.  
- 🔹 **Matriz de Confusión** de clasificadores.  
- 🔹 **Comparación de métricas de regresión y clasificación**.  

## 📝 Reflexiones del Ejercicio
- 📌 Los modelos lineales y polinómicos **no son adecuados** para este problema: mostraron R² muy bajos o negativos.  
- 📌 **Árboles de Decisión y Random Forest** ofrecieron el mejor rendimiento al capturar interacciones complejas.  
- 📌 Los modelos de clasificación **KNN y Árbol** separaron de forma confiable los países según impacto climático, mientras que **SVM tuvo dificultades** incluso tras optimización.  
- 📌 La optimización con **GridSearchCV** mejoró ligeramente SVM, pero quedó limitado por el tamaño del dataset.  
- 📌 Estos resultados sugieren que **la seguridad alimentaria global se analiza mejor con modelos basados en árboles**, ya que permiten interpretar relaciones no lineales entre clima y producción agrícola.  

---

✍️ *Autor: Liroy Cataldo*

