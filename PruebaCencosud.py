from pyspark import SparkContext, SparkConf, SQLContext
import json

appName = 'Prueba Cencosud'
master = 'local[*]'

conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

def run():
    ##Primero se determina donde esta el archivo CSV, en este caso es en este path
    pathCSV = "/home/francisco/Documentos/TestCencosud/PruebaCencosud/csv/retail-food-stores_Fix6.csv"

    ##Se define la variable del DataFrame llamada df que contiene la lectura del CSV
    ##Se intenta corregir el CSV modificandolo, aplicando separador por TAB para que al leer el campo Location no se corte el JSON
    df = sqlContext.read.option("delimiter", "\\t").csv(pathCSV)
    df.printSchema()

    ##Se selecciona la columna Location (15) y se muestra su contenido
    ##Location = df.select(df._c14)
    ##Location.show()
    df.registerTempTable("datos")
    df14 = sqlContext.sql("SELECT _c14 AS Location FROM datos")
    ##df14.show()
    ##df14.coalesce(1).write.json("retail-food-stores.json")
    
    ##La columna Location
    dfLocation = sqlContext.read.json(df14.na.replace('\"', '"').rdd)
    dfLocation.show()
    dfLocation.printSchema()
    dfLocation.coalesce(1).write.json("retail-food-stores.json")

    dfLatitude = sqlContext.read.json(df14.na.replace('\"', '"').rdd).select("latitude")
    dfLatitude.show()

    dfLongitude = sqlContext.read.json(df14.na.replace('\"', '"').rdd).select("longitude")
    dfLongitude.show()
    
    ##Escribe el resultado en un JSON para revisar
    ##new_df.coalesce(1).write.json("retail-food-stores.json")

    ##Borra la columna Location y escribir archivo resultado ORC
    ##df.drop(df._c14).coalesce(1).write.format("orc").mode("overwrite").save("retail-food-stores.orc")


if __name__ == "__main__":
    run()
