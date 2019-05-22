# PruebaCencosud
_Este proyecto es una prueba para postular a Cencosud._

### Pre-requisitos 📋

_Un sistema Unix/Linux como por ejemplo Ubuntu 18.04_
_La máquina Virtual de Java_
_Apache Spark_
_pyspark_

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


## Construido con 🛠️

Para el desarrollo se utilizó terminal de Ubuntu, Spark y Visual Studio Code
* [Spark](https://spark.apache.org/) - Framework de computación en clúster open-source
* [VS Code](https://code.visualstudio.com/) - IDE para programar el PySpark
