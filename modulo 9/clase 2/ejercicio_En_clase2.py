
import findspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
import os

findspark.init()

#Creamos sesión Spark
spark=SparkSession.builder.appName("AnalisisAppMovil").getOrCreate()

print("SparkSesion creada con exito")

#Cargar el conjunto de datos

data=[("user_1","Android",120),
      ("user_2","iOS",300),
      ("user_3","Android",150),
      ("user_4","iOS",250),
      ("user_5","Android",90),
      ("user_6","iOS",400),
      ("user_7","Android",180),
      ("user_8","iOS",220)]


columnas=["user_id","tipo_dispositivo", "duracion_sesion"]

df_app=spark.createDataFrame(data,columnas)
print("Contenido DF inicial")
df_app.show()

#Agrupar datos por dispositivo
df_agrupado=df_app.groupBy("tipo_dispositivo")

#Calcular el promedio de columna "duracion_sesion" para c/grupo
df_promedio = df_agrupado.agg(avg("duracion_sesion").alias("promedio_duracion_sesion"))

print("Duración promedio de sesión por tipo de dispositivo")
df_promedio.show()

df_promedio.write.mode("overwrite").option("header","true").csv("duracion_promedio_app.csv")
print("Resultados guardados satisfactoriamente")


