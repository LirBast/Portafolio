
import findspark #para que Python encuentre PySpark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

#Configurar Spark para que encuentre el entorno
findspark.init()

#Crear sesión

spark=SparkSession.builder \
    .appName("AnalisisVentas") \
    .getOrCreate()

#Verificar que la sesión se haya creado exitosamente
print("SparkSesion creada con éxito")

data=[("Producto A", 100, 15.50, "2023-01-01"),
      ("Producto B", 50, 30.00, "2023-01-01"),
      ("Producto C", 150, 5.00, "2023-01-02"),
      ("Producto A", 20, 15.50, "2023-01-02"),
      ("Producto B", 75, 20.00, "2023-01-03"),
      ("Producto A", 125, 15.50, "2023-01-04"),
      ("Producto C", 200, 5.00, "2023-01-04")
       ]

columnas=["producto", "cantidad", "precio", "fecha"]

#Convertir en un DF de PySpark

df_ventas=spark.createDataFrame(data, columnas)

#Mostrar el contenido del DF
print("Contenido del DF de ventas")
df_ventas.show()

# #Filtrado y Agrupamiento
# #Filtrar solo las filas donde la columna 'producto' es igual a 'Producto A
# df_producto_a=df_ventas.filter(df_ventas.producto=="Producto A")

# print("DataFrame filtado para 'Producto A':")
# df_producto_a.show()

# #Agrupar los datos del 'Producto A' por la columna 'fecha' y sumar la columna 'cantidad'
# df_agrupado=df_producto_a.groupBy("fecha").sum("cantidad")

# print("Ventas totales de 'Producto A' por fecha:" )
# df_agrupado.show()

# #Crear columna ingresos
# df_ingresos=df_ventas.withColumn("ingresos",col("cantidad") * col("precio"))

# print("DF con la columna 'ingresos:")
# df_ingresos.show()

# #Agrupar el DF por la columna "producto" y sumar la nueva columna ingresos
# df_ingresos_totales=df_ingresos.groupBy("producto").sum("ingresos")

# df_ingresos_totales.show()

# #Renombrar la columna de suma para que sea más clara
# df_ingresos_totales=df_ingresos_totales.withColumnRenamed("sum(ingresos)","ingresos totales")

# #Ingresos totales por producto
# df_ingresos_totales.show()

# #Guardar el DF df_ingresos_totales en un archivo csv

# df_ingresos_totales.write.mode("overwrite").option("header","true").csv("ingresos_totales_por_producto.csv")

# print("Resultados guardados exitosamente")

