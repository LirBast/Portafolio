import os
import numpy as np
import kagglehub
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Download latest version
path = kagglehub.dataset_download("salader/dogs-vs-cats")

print("Path to dataset files:", path)
print("Archivos disponibles:", os.listdir(path))


train_dir = 'C:\Users\liroy\.cache\kagglehub\datasets\salader\dogs-vs-cats\versions\1\train'
validation_dir = 'C:\Users\liroy\.cache\kagglehub\datasets\salader\dogs-vs-cats\versions\1\test'

# Parámetros para la carga de datos

IMG_WIDTH = 150
IMG_HEIGHT = 150
BATCH_SIZE = 32

train_data_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,   # Corrige el typo y agrega un valor (ejemplo: 0.2)
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

validation_data_gen = ImageDataGenerator(rescale = 1./255)

train_generator = train_data_gen.flow_from_directory()