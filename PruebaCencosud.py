from pyspark import SparkContext, SparkConf, SQLContext
import json

appName = 'Prueba Cencosud'
master = 'local[*]'

conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

def run():
    ##Primero se determina donde esta el archivo CSV, en este caso es en este path
    pathCSV = "/home/francisco/Documentos/TestCencosud/PruebaCencosud/csv/retail-food-stores.csv"

    ##Se define la variable del DataFrame llamada df que contiene la lectura del CSV
    df = sqlContext.read.csv(pathCSV)

    ##Se selecciona la columna Location (15) y se muestra su contenido
    df.select(df._c14).show()

if __name__ == "__main__":
    run()
