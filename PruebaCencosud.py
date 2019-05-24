from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import lit
import json

appName = 'Prueba Cencosud'
master = 'local[*]'

conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

def run():
    print("Comienzo del Ejercicio")

    ##Path donde esta el archivo CSV a procesar, aca se puede poner la ruta donde el usuario tenga el archivo
    pathCSV = "/home/francisco/Documentos/TestCencosud/PruebaCencosud/csv/retail-food-stores.csv"

    ##Se define la variable del DataFrame llamada df que contiene la lectura del CSV
    df = sqlContext.read.option("delimiter", ",").csv(pathCSV) ##\\t
    ##df.printSchema()                  ##Despliega el schema del DataFrame
    ##dfLocation.show()                 #Despliega el contenido del DataFrame

    ##Se obtiene el rdd del CSV para procesarlo
    rdd = sc.textFile(pathCSV)

    ##Se transforma el rdd reemplazando, separando y joineando los valores para establecer un JSON valido
    rdd2=rdd.map(lambda x: x.replace("'", "\"").replace('""', '"').replace('False', '"false"').strip()) \
            .map(lambda x: x.split(',')) \
            .map(lambda x: ''.join(x[14:21])) \
            .map(lambda x: x.replace('"{','{').replace('}"','}').replace('""','","').replace('} "', '} ,"').replace('" "', '", "'))
    
    ##Se obtiene la columna Location como un JSON
    dfLocation = sqlContext.read.json(rdd2)
    ##dfLocation.printSchema()
    ##dfLocation.show()

    ##Escribe el resultado en un JSON para revisar
    dfLocation.coalesce(1).write.format("json").mode("overwrite").save("retail-food-stores.json")

    ##Se obtiene campo latitude del JSON
    dfLatitude = dfLocation.select("latitude")
    ##dfLatitude.printSchema()
    ##dfLatitude.show()

    ##Se obtiene campo longitude del JSON
    dfLongitude = dfLocation.select("longitude")
    ##dfLongitude.printSchema()
    ##dfLongitude.show()

    ##Borra la columna Location y agrega latitude y longitude en el DataFrame
    df = df.drop(df._c14)
    df = df.withColumn("latitude", lit(dfLatitude["latitude"]))
    ##df.printSchema()
    df = df.withColumn("longitude", lit(dfLongitude["longitude"]))
    ##df.printSchema()

    ##Escribe el resultado en archivo ORC
    df.coalesce(1).write.format("orc").mode("overwrite").save("retail-food-stores.orc")

    print("Fin del Ejercicio")

if __name__ == "__main__":
    run()
