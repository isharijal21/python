"""
Car Power Analysis
Problem Statement
As a data engineer you are given the task to transform the given data
In addition to given metadata, transformed data should have a column named as AvgWeight with constant value as 200 and also kilowatt_power which needs to be 1000 times horsepower.
Column name carr is a misspelled column name, and you are supposed to correct this to car

Data
Ford Torino, 140, 3449, US
Chevrolet Monte Carlo, 150, 3761, US
BMW 2002, 113, 2234, Europe


Metadata- columns
carr - String
horsepower - Integer
weight - Integer
origin - String
"""

from pyspark.sql.functions import col,lit
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField,IntegerType,StringType

if __name__ == "__main__":
    spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

    data =[
        ("Ford Torino", 140, 3449, "US"),
         ("Chevrolet Monte Carlo", 150, 3761,"US"),
         ("BMW 2002" , 113, 2234, "Europe" )
    ]
    columns = ["carr", "horsepower", "weight", "origin"]
    schema = StructType([
        StructField('carr', StringType(), True),
        StructField('horsepower', IntegerType(), True),
        StructField('weight', IntegerType(), True),
        StructField('origin', StringType(), True)
    ])

    df = spark.createDataFrame(data=data, schema=columns)
    df.show(truncate=False)
    print("==========================")
    #CREATES A NEW COLUMN WITH A CONSTANT VALUE OF 200
    df.withColumn("AvgWeight", lit("200")).show()
    print("==========================")
    #UPDATES THE VALUE OF HORSEPOWER
    udf = df.withColumn("horsepower", col("horsepower") * 1000)
    udf.show(truncate=False)
    # UPDATES THE MISSPELLED COLUMN NAME "CARR" to "CAR"
    df.withColumnRenamed("carr", "car") \
        .show(truncate=False)












