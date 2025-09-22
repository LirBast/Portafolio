import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

def predict_new_review(modelo, tokenizer, review_text, max_length=200):
  new_sequence=tokenizer.texts_to_sequences([review_text])
  new_padded=pad_sequences(new_sequence, maxlen=max_length, padding='post', truncating='post')
  prediction=modelo.predict(new_padded)
  proba=prediction[0][0]
  if proba >0.5:
    sentiment='positiva'
  else:
    sentiment='negativo'
  return sentiment, proba

model_path = r"C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 8\clase 4\LSTM_review_model.h5"
tokenizer_path = r"C:\Users\liroy\OneDrive\Escritorio\bootcamp\proyecto\modulo 8\clase 4\tokenizer.pickle"

loaded_model = tf.keras.models.load_model(model_path)
with open(tokenizer_path, "rb") as handle:
    tokenizer = pickle.load(handle)


# try:
#   loaded_model=tf.keras.models.load_model('LSTM_review_model.h5')
#   print('Modelo review.h5 cargado exitosamente')

# except Exception as e:
#   print(f'Error en cargar el modelo: {e}')
#   loaded_model=None

# try:
#   with open ('tokenizer.pickle', 'rb') as handle:
#     tokenizer = pickle.load(handle)
#   print('Tokenizador cargado exitosamente')

# except Exception as e:
#   print(f'Error en cargar el modelo: {e}')
#   tokenizer=None

if loaded_model and tokenizer:
  new_review='This movie was absolutely fantastic. The acting was superb and the story was very compelling'
  MAX_LENGTH=200
  sentimiento_predicho, probabilidad_predicha=predict_new_review(loaded_model, tokenizer, new_review, MAX_LENGTH)
  print(f'Nueva reseña:{new_review}')
  print(f'Sentimiento predicho: {sentimiento_predicho}')
  print(f'Probabilidad predicha: {probabilidad_predicha}')