from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import lit, exp
import json

appName = 'Prueba Cencosud'
master = 'local[*]'

conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

def run():
    print("Comienzo del Ejercicio")

    ##Path donde esta el archivo CSV a procesar, aca se puede poner la ruta donde el usuario tenga el archivo
    pathCSV = "/home/francisco/Documentos/TestCencosud/PruebaCencosud/csv/clean_test.csv"

    ##Se define la variable del DataFrame llamada df que contiene la lectura del CSV
    df = sqlContext.read.option("delimiter", "|").csv(pathCSV)

    ##Se obtiene el rdd del CSV para procesarlo
    rdd = sc.textFile(pathCSV)

    ##Se transforma el rdd y se obtiene la columna Location como un JSON valido
    rdd2=rdd.map(lambda x: x.split('|')[13])
    dfLocation = sqlContext.read.json(rdd2)

    ##Escribe la columna Location en un JSON
    dfLocation.coalesce(1).write.format("json").mode("overwrite").save("resultado.json")

    ##Se obtiene campo latitude del JSON
    dfLatitude = dfLocation.select("latitude")

    ##Se obtiene campo longitude del JSON
    dfLongitude = dfLocation.select("longitude")

    ##Borra la columna Location y agrega latitude y longitude en el DataFrame
    df = df.drop(df._c13)
    ##df = df.withColumn("latitude", dfLatitude["latitude"])
    ##df.printSchema()
    ##df = df.withColumn("longitude", lit(dfLongitude["longitude"]))
    ##df.printSchema()

    ##Escribe el resultado en archivo ORC
    df.coalesce(1).write.format("orc").mode("overwrite").save("resultado.orc")

    print("Fin del Ejercicio")

if __name__ == "__main__":
    run()
