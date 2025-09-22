import os
import numpy as np
import kagglehub
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Descarga el dataset y obtiene la ruta base
path = kagglehub.dataset_download("salader/dogs-vs-cats")

# Define rutas de entrenamiento y validación
train_dir = os.path.join(path, "train")
validation_dir = os.path.join(path, "test")

# Verifica estructura de carpetas
print("Train subfolders:", os.listdir(train_dir))
print("Validation subfolders:", os.listdir(validation_dir))

# Parámetros para la carga de datos
IMG_WIDTH = 150
IMG_HEIGHT = 150
BATCH_SIZE = 32

# Generadores de datos con aumentos para entrenamiento y solo rescale para validación
train_data_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

validation_data_gen = ImageDataGenerator(rescale=1./255)

# Carga de datos desde directorios
train_generator = train_data_gen.flow_from_directory(
    train_dir,
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode='binary')

validation_generator = validation_data_gen.flow_from_directory(
    validation_dir,
    target_size=(IMG_WIDTH, IMG_HEIGHT),
    batch_size=BATCH_SIZE,
    class_mode='binary')

model = Sequential()
# Primera capa convolucional y pooling (nota: kernel_size = (3,3))
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)))
model.add(MaxPooling2D((2, 2)))

# Segunda capa convolucional y pooling
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

# Tercera capa convolucional y pooling
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

# Cuarta capa convolucional y pooling
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

# Aplanar la salida de las capas convolucionales
model.add(Flatten())
# Capa de regularización
model.add(Dropout(0.5))
# Capa densa
model.add(Dense(512, activation='relu'))
# Capa de salida
model.add(Dense(1, activation='sigmoid'))

# Resumen del modelo
model.summary()

# Compilado
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Parámetros de entrenamiento
epocas = 20

# Entrenamiento
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=epocas,
    validation_data=validation_generator,
    validation_steps=len(validation_generator)
)

# Visualizar precisión (accuracy)
plt.figure(figsize=(10, 6))
plt.plot(history.history['accuracy'], label='Precisión entrenamiento')
plt.plot(history.history['val_accuracy'], label='Precisión validación')
plt.title('Precisión: entrenamiento vs validación')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.legend()
plt.show()

# Visualizar pérdida (loss)
plt.figure(figsize=(10, 6))
plt.plot(history.history['loss'], label='Pérdida entrenamiento')
plt.plot(history.history['val_loss'], label='Pérdida validación')
plt.title('Pérdida: entrenamiento vs validación')
plt.xlabel('Épocas')
plt.ylabel('Pérdida')
plt.legend()
plt.show()