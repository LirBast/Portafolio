# 🎓 Módulo 5 – Diseño y Análisis de un Experimento sobre el Rendimiento Académico

Este proyecto corresponde al **Módulo 5 del Bootcamp de Ciencia de Datos**.  
El objetivo fue **evaluar estadísticamente si un nuevo programa de tutoría mejora el rendimiento académico de los estudiantes**, aplicando conceptos de diseño experimental, estadística descriptiva, pruebas de hipótesis e intervalos de confianza.

## 📂 Contenido
- `rendimiento_academico.py`: Script en Python con el análisis completo.  
- `graficos/`: Carpeta con histogramas y diagramas de caja generados en el experimento.  

## 🛠️ Tecnologías usadas
- Python (NumPy, SciPy, Matplotlib)  
- Estadística Inferencial y Pruebas de Hipótesis  

## 📋 Requerimientos implementados
1. **🧪 Diseño del Experimento**  
   - Grupo A (15 estudiantes): recibió el programa de tutoría.  
   - Grupo B (15 estudiantes): grupo de control.  
   - Propuesta de mejoras al diseño para reducir sesgos:  
     - Aumentar el tamaño de la muestra.  
     - Medir el rendimiento previo de los estudiantes.  
     - Asegurar asignación completamente aleatoria.  

2. **📊 Estadísticas Descriptivas**  
   - Media y desviación estándar de ambos grupos.  
   - Histogramas de distribución de calificaciones por grupo.  
   - Diagrama de caja comparativo para detectar diferencias y outliers.  

3. **📈 Prueba de Hipótesis (t-test)**  
   - Hipótesis nula (H0): no hay diferencia en el rendimiento académico entre los grupos.  
   - Hipótesis alternativa (H1): el grupo con tutoría tiene mejor rendimiento.  
   - Prueba t para muestras independientes con α = 0.05.  
   - Interpretación del valor p y decisión estadística.  

4. **📉 Intervalo de Confianza (95%)**  
   - Intervalo de confianza para la diferencia de medias entre Grupo A y Grupo B.  
   - Interpretación de la magnitud de la mejora atribuida al programa de tutoría.  

## 🎯 Resultados principales
- **Grupo A (Tutoría):**  
  - Media ≈ 86.0 | Desviación estándar ≈ 3.9  
- **Grupo B (Control):**  
  - Media ≈ 74.7 | Desviación estándar ≈ 3.6  

- La prueba t arrojó un valor **p < 0.05**, lo que permitió **rechazar H0** y concluir que el programa de tutoría **sí mejora el rendimiento académico**.  
- El **intervalo de confianza del 95%** para la diferencia de medias fue aproximadamente **[7.9 , 13.7]**, confirmando que los estudiantes con tutoría obtuvieron entre **8 y 14 puntos más** que los del grupo de control.  

## 📊 Visualizaciones
Algunas de las visualizaciones generadas en este módulo:  

![Histograma Grupo A](img/mod5_histograma_a.png)  
![Histograma Grupo B](img/mod5_histograma_b.png)  
![Boxplot comparativo](img/mod5_boxplot.png)  

---

✍️ *Autor: Liroy Cataldo*

