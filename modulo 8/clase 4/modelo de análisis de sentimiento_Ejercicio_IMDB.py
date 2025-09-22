import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense, Dropout
import kagglehub
import matplotlib.pyplot as plt

# Download latest version
path = kagglehub.dataset_download("lakshmi25npathi/imdb-dataset-of-50k-movie-reviews")

print("Path to dataset files:", path)

# Ruta al archivo CSV del dataset
archivos = os.listdir(path)
print(f"Archivos disponibles: {archivos}")

# Cargar el dataset
dataset_path = os.path.join(path, 'IMDB Dataset.csv')
df = pd.read_csv(dataset_path)

# Exploración inicial de los datos
print(df.head())       # Mostrar las primeras filas para ver la estructura
print("\n" + "="*80 + "\n")
print(df.info())       # Información general: tipos de datos y valores nulos
print("\n" + "="*80 + "\n")
print(df.describe())   # Estadísticas descriptivas básicas
print("\n" + "="*80 + "\n")

X=df['review']
y=df['sentiment']

le=LabelEncoder()
y=le.fit_transform(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=42)

tokenizer=Tokenizer(num_words=10000,oov_token='<OOV>')
tokenizer.fit_on_texts(X_train)

X_train_sequences=tokenizer.texts_to_sequences(X_train)
X_test_sequences=tokenizer.texts_to_sequences(X_test)

max_length=200

X_train_pad=pad_sequences(X_train_sequences, maxlen=max_length, padding='post', truncating='post')
X_test_pad=pad_sequences(X_test_sequences, maxlen=max_length, padding='post', truncating='post')

print('\nEjemplo de secuencia tokenizada y con padding\n')
print(f'Secuencia original: {X_train_sequences[0][:10]}')
print(f'Secuencia con padding: {X_train_pad[0][:10]}')
print(f'Longitud de la secuencia: {len(X_train_pad[0])}')

VOC_SIZE=10000
EMBEDDING_DIM=128
RRN_UNITS=64

model=Sequential()
model.add(Embedding(VOC_SIZE, EMBEDDING_DIM))
model.add(SimpleRNN(RRN_UNITS))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print('\nResumen de la arquitectura del modelo\n')
model.build(input_shape=(None, max_length))
model.summary()

history=model.fit(X_train_pad,y_train, epochs=5, batch_size=32, validation_data=(X_test_pad, y_test))
loss, accuracy=model.evaluate(X_test_pad, y_test, verbose=0)
print('Resultado de la evaluacion en el conjunto de prueba')
print(f'Pérdida: {loss:.4f}')
print(f'Precisión: {accuracy:.4f}')

plt.figure(figsize=(12, 5))

plt.subplot(1,2,1)
plt.plot(history.history['accuracy'], label='Precisión de entrenamiento')
plt.plot(history.history['val_accuracy'], label='Precisión de validación')
plt.title('Precisión de entrenamiento vs validación')
plt.xlabel('Épocas')
plt.ylabel('Precisión')
plt.legend()


plt.subplot(1,2,2)
plt.plot(history.history['loss'], label='Perdida de entrenamiento')
plt.plot(history.history['val_loss'], label='Perdida de validación')
plt.title('Perdida de entrenamiento vs validación')
plt.xlabel('Épocas')
plt.ylabel('Perdida')
plt.legend()

plt.tight_layout()
plt.show()

new_review="This film is a boring, nonsensical mess. A two-hour assault on the senses, it stumbles from one cliché to the next, with laughable dialogue and laughably stiff acting. The action is a chaotic blur. Save yourself the trouble; you'll thank me later"

new_review_sequences=tokenizer.texts_to_sequences([new_review])
new_review_pad=pad_sequences(new_review_sequences, maxlen=max_length, padding='post', truncating='post')
prediccion=model.predict(new_review_pad)[0][0]

sentimiento='Positiva' if prediccion>0.5 else 'Negativa'
print('\nPrediccion de una nueva reseña\n')
print(f'Reseña: {new_review}')
print(f'Probabilidad de ser positiva: {prediccion:.4f}')
print(f'El modelo predice que la reseña es: {sentimiento}')
