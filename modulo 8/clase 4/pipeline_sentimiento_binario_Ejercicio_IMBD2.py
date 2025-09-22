import os
import pandas as pd
import kagglehub
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense, Dropout

# Descargar la última versión del dataset
path = kagglehub.dataset_download("lakshmi25npathi/imdb-dataset-of-50k-movie-reviews")
print("Ruta a los archivos del dataset:", path)

# Listar archivos disponibles
archivos = os.listdir(path)
print(f"Archivos disponibles: {archivos}")

# Cargar el dataset
dataset_path = os.path.join(path, 'IMDB Dataset.csv')
df = pd.read_csv(dataset_path)

# Exploración inicial de los datos
print(df.head())       # Primeras filas
print("\n" + "="*80 + "\n")
print(df.info())       # Información general
print("\n" + "="*80 + "\n")
print(df.describe())   # Estadísticas descriptivas
print("\n" + "="*80 + "\n")

# Análisis de la distribución de clases (sentiment)
print('Conteo de Clases')
class_counts = df['sentiment'].value_counts()
print(class_counts)

# Separar variables
X = df['review']
y = df['sentiment']

# Codificar etiquetas (neg/pos -> 0/1)
le = LabelEncoder()
y = le.fit_transform(y)

# Partición de datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Tokenización
tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(X_train)

# Secuencias y padding
X_train_sequences = tokenizer.texts_to_sequences(X_train)
X_test_sequences = tokenizer.texts_to_sequences(X_test)

max_length = 200
X_train_pad = pad_sequences(X_train_sequences, maxlen=max_length, padding='post', truncating='post')
X_test_pad = pad_sequences(X_test_sequences, maxlen=max_length, padding='post', truncating='post')

print('\nEjemplo de secuencia tokenizada y con padding\n')
print(f'Secuencia original (primeros 10 tokens): {X_train_sequences[0][:10]}')
print(f'Secuencia con padding (primeros 10): {X_train_pad[0][:10]}')
print(f'Longitud de la secuencia: {len(X_train_pad[0])}')

# Hiperparámetros
VOC_SIZE = 10000
EMBEDDING_DIM = 128
RRN_UNITS = 64


# Construcción del modelo con dropout mejorado
model = Sequential()
model.add(Embedding(VOC_SIZE, EMBEDDING_DIM, input_length=max_length))
# Dropout después del embedding
model.add(Dropout(0.2))
# SimpleRNN con dropout interno para mejor regularización
model.add(SimpleRNN(RRN_UNITS, dropout=0.3, recurrent_dropout=0.3))
# Dropout antes de la capa densa final
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# Compilación del modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print('\nResumen de la arquitectura del modelo\n')
model.summary()

# Entrenamiento del modelo
print('\nIniciando entrenamiento...\n')
history = model.fit(
    X_train_pad, y_train,
    epochs=5,
    batch_size=32,
    validation_data=(X_test_pad, y_test),
    verbose=1
)

# Evaluación final
print('\nEvaluación en conjunto de prueba:')
test_loss, test_accuracy = model.evaluate(X_test_pad, y_test, verbose=0)
print(f'Exactitud en test: {test_accuracy:.4f}')
print(f'Pérdida en test: {test_loss:.4f}')