from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

# 1. Crear la sesión de Spark para el procesamiento agrícola
spark = SparkSession.builder \
    .appName("ProcesamientoBatchAgricola") \
    .getOrCreate()

# 2. Cargar el archivo CSV agrícola que descargaste
# Asegúrate de que el archivo esté en la misma carpeta y pon su nombre exacto aquí:
ruta_dataset = "pesticides.csv" 
df = spark.read.option("header", "true").option("inferSchema", "true").csv(ruta_dataset)

# 3. Análisis Exploratorio Básico (EDA) requerido por la guía
print("--- ESTRUCTURA DE LAS COLUMNAS ---")
df.printSchema()

print("--- PRIMERAS FILAS DEL DATASET AGRÍCOLA ---")
df.show(5)

# 4. Procesamiento en Batch: Limpieza de datos (eliminar filas vacías)
df_limpio = df.dropna()
print(f"Total de registros analizados sin errores: {df_limpio.count()}")

# 5. Ejemplo de transformación y agregación de datos agrícolas
print("--- RESULTADOS DEL PROCESAMIENTO ---")
# Esto agrupa por el primer campo disponible o categoría para mostrar un resumen en consola
df_limpio.describe().show()

# Opcional: Mostrar un resumen ordenado si el dataset tiene categorías o países
# df_limpio.groupBy("Area").count().show(10)