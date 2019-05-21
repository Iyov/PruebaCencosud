from pyspark import SparkContext, SparkConf, SQLContext
import json

appName = 'Prueba Cencosud'
master = 'local[*]'

conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

def run():
    ##print("Aca comienzo la lectura del CSV")
    df = sqlContext.read.csv("/home/francisco/Documentos/PruebaCencosud/csv/retail-food-stores.csv")
    df.show()


if __name__ == "__main__":
    run()
