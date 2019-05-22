# PruebaCencosud
_Este proyecto es una prueba para postular a Cencosud._

### Pre-requisitos 📋

_Un sistema Unix/Linux como por ejemplo Ubuntu 18.04_
La máquina Virtual de Java
Apache Spark
pyspark

## Requerimientos 🚀

Se requiere leer un DataSet público de Kaggle llamado "NYS Retail Food Stores", su URL es https://www.kaggle.com/new-york-state/nys-retail-food-stores y el archivo se denomina "retail-food-stores.csv" utilizando Spark y Python (pyspark) transformando el campo Location (JSON) en Latitud y Longitud y eliminando la Location.

### Instalación 🔧

Actualizar sistema:
```sudo apt update```
Instalar JDK:
```sudo apt install -y default-jdk```
Instalar pip:
```apt install python-pip```
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
```pip install pyspark```

## Ejecutando las pruebas ⚙️

Ir a la carpeta donde está el archivo Python (.py) y luego ejecutarlo
```
  cd /home/francisco/Documentos/TestCencosud/PruebaCencosud/
  python PruebaCencosud.py
 ```

## Construido con 🛠️

Se utilizó terminal de Ubuntu, Spark y Visual Studio Code
* [Spark](https://spark.apache.org/) - Framework de computación en clúster open-source
* [VS Code](https://code.visualstudio.com/) - IDE para programar el PySpark
