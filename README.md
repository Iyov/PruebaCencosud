# PruebaCencosud
_Este proyecto es una prueba para postular a Cencosud._

### Pre-requisitos 📋

Un sistema Unix/Linux como por ejemplo Ubuntu 18.04.

La máquina Virtual de Java.

Apache Spark.

pyspark.


## Requerimientos 🚀

Se requiere leer un DataSet público de Kaggle llamado "NYS Retail Food Stores", su URL es https://www.kaggle.com/new-york-state/nys-retail-food-stores y el archivo se denomina "retail-food-stores.csv" utilizando Spark y Python (pyspark) transformando el campo Location (JSON) en Latitud y Longitud y eliminando la Location.

### Instalación 🔧

Actualizar sistema:
```
    sudo apt update
```
Instalar JDK:
```
    sudo apt install -y default-jdk
```
Instalar pip:
```
    apt install python-pip
```
Instalar Spark:
```
    sudo apt install wget
    wget https://www-eu.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz
    mkdir -p /home/spark
    cd /home/spark
    tar xzvf spark-2.4.3-bin-hadoop2.7.tgz
    mv spark-2.4.3-bin-hadoop2.7 spark
    export SPARK_HOME=/home/spark/spark
    cd /home/spark/spark
```
Instalar pyspark:
```
    pip install pyspark
```

## Ejecutando las pruebas ⚙️

Ir a la carpeta donde está el archivo Python (.py) y luego ejecutarlo
```
    cd /home/francisco/Documentos/TestCencosud/PruebaCencosud/
    python PruebaCencosud.py
```

## Comentarios
Al leer y procesar el DataSet "retail-food-stores.csv" tuve inconvenientes al momento de intentar leer/transformar el campo Location, como era un archivo CSV se cortaba el registro del JSON, solo mostrandome una parte y no el total.
Intenté modificarlo arreglando el JSON, reemplazando los caracteres que lo hacían inválidos en el archivo ```/PruebaCencosud/csv/retail-food-stores_Fix.csv``` y no tuve buenos resultados. También haciendo que el separador del CSV sea un tabulador, como está actualmente en el archivo ```/PruebaCencosud/csv/retail-food-stores_Fix2.csv``` pero tampoco tuve buenos resultados.
Intente de 4 maneras distintas modificar el Location del CSV pero no me funcionó, me arroja este error al procesar el JSON:
```
    root
 |-- _corrupt_record: string (nullable = true)

Traceback (most recent call last):                                              
  File "PruebaCencosud.py", line 48, in <module>
    run()
  File "PruebaCencosud.py", line 34, in run
    dfLatitude = sqlContext.read.json(df14.na.replace('\"', '"').rdd).select("latitude")
  File "/usr/local/lib/python2.7/dist-packages/pyspark/sql/dataframe.py", line 1320, in select
    jdf = self._jdf.select(self._jcols(*cols))
  File "/usr/local/lib/python2.7/dist-packages/py4j/java_gateway.py", line 1257, in __call__
    answer, self.gateway_client, self.target_id, self.name)
  File "/usr/local/lib/python2.7/dist-packages/pyspark/sql/utils.py", line 69, in deco
    raise AnalysisException(s.split(': ', 1)[1], stackTrace)
pyspark.sql.utils.AnalysisException: u"cannot resolve '`latitude`' given input columns: [_corrupt_record];;\n'Project ['latitude]\n+- LogicalRDD [_corrupt_record#67], false\n"
```


## Construido con 🛠️

Para el desarrollo se utilizó terminal de Ubuntu, Spark y Visual Studio Code
* [Spark](https://spark.apache.org/) - Framework de computación en clúster open-source
* [VS Code](https://code.visualstudio.com/) - IDE para programar el PySpark
