from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

y_true = [1, 0, 1, 1, 0, 0, 1]            # etiquetas reales
y_pred = [1, 0, 0, 1, 0, 1, 1]            # predicciones (clase discreta)

# Matriz de confusión binaria (por defecto, ordena por clase 0 luego 1)
cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
print("Matriz de confusión (filas=real, columnas=pred):\n", cm)

# Reporte con precision, recall, f1 por clase
print(classification_report(y_true, y_pred, target_names=["negativo", "positivo"]))

# Visualización
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["negativo","positivo"])
disp.plot(cmap="Blues")
plt.show()