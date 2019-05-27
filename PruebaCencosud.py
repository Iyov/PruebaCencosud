from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import *
import json

appName = 'Prueba Cencosud'
master = 'local[*]'

conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

def ejercicio():
    print("Comienzo del Ejercicio")
    
    ##Path donde esta el archivo CSV a procesar, aca se puede poner la ruta donde el usuario tenga el archivo
    pathCSV = "/home/francisco/Documentos/TestCencosud/PruebaCencosud/csv/clean_test.csv"

    ##Se define la variable del DataFrame llamada df que contiene la lectura del CSV
    df = sqlContext.read.option("delimiter", "|").csv(pathCSV)
    
    ##Obtiene latitude y longitude como JSON y las agrega, Borra la columna Location
    df = df.withColumn("latitude", get_json_object(df["_c13"],"$.latitude").alias("latitude"))
    df = df.withColumn("longitude", get_json_object(df["_c13"],"$.longitude").alias("longitude"))
    df = df.drop("_c13")

    ##Escribe el resultado en archivo CSV y ORC
    df.coalesce(1).write.format("csv").mode("overwrite").save("resultado.csv")
    df.coalesce(1).write.format("orc").mode("overwrite").save("resultado.orc")

    print("Fin del Ejercicio")

if __name__ == "__main__":
    ejercicio()
