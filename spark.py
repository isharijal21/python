from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import col,lit



def wordCount(spark, filepath):
    rdd = spark.sparkContext.textFile(filepath)
    rdd2 = rdd.flatMap(lambda x: x.split(" "))
    rdd3 = rdd2.map(lambda x: (x, 1))
    rdd5 = rdd3.reduceByKey(lambda a, b: a + b)
    print(rdd5.collect())


if __name__ == "__main__":

        spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

        data = [("James", "Smith", "USA", "CA"),
                ("Michael", "Rose", "USA", "NY"),
                ("Robert", "Williams", "USA", "CA"),
                ("Maria", "Jones", "USA", "FL")
                ]
        columns = ["firstname", "lastname", "country", "state"]
        df = spark.createDataFrame(data=data, schema=columns)
        df.show(truncate=False)
        #Select Single & Multiple Columns From PySpark

        df.select("firstname", "lastname").show()

        df.select(df.firstname, df.lastname).show()

        df.select(df["firstname"], df["lastname"]).show()

        # By using col() function



        df.select(col("firstname"), col("lastname")).show()

        # Select All
        df.select("*").show()

        # Selects first 3 columns and top 3 rows
        df.select(df.columns[:3]).show(3)

        # Selects columns 2 to 4  and top 3 rows
        df.select(df.columns[2:4]).show(3)
        print('=============================')

        #Select Nested Struct Columns from PySpark

        data = [
            (("James", None, "Smith"), "OH", "M"),
            (("Anna", "Rose", ""), "NY", "F"),
            (("Julia", "", "Williams"), "OH", "F"),
            (("Maria", "Anne", "Jones"), "NY", "M"),
            (("Jen", "Mary", "Brown"), "NY", "M"),
            (("Mike", "Mary", "Williams"), "OH", "M")
        ]
        schema = StructType([
            StructField('name', StructType([
                StructField('firstname', StringType(), True),
                StructField('middlename', StringType(), True),
                StructField('lastname', StringType(), True)
            ])),
            StructField('state', StringType(), True),
            StructField('gender', StringType(), True)
        ])

        df2 = spark.createDataFrame(data=data, schema=schema)
        df2.printSchema()
        df2.show(truncate=False)  # shows all columns
        df2.select("name").show(truncate=False)

        #particular column filter
        df2.select("name.firstname", "name.lastname").show(truncate=False)
        #withColumn()
        data = [('James', '', 'Smith', '1991-04-01', 'M', 3000),
                ('Michael', 'Rose', '', '2000-05-19', 'M', 4000),
                ('Robert', '', 'Williams', '1978-09-05', 'M', 4000),
                ('Maria', 'Anne', 'Jones', '1967-12-01', 'F', 4000),
                ('Jen', 'Mary', 'Brown', '1980-02-17', 'F', -1)
                ]

        columns = ["firstname", "middlename", "lastname", "dob", "gender", "salary"]

        df = spark.createDataFrame(data=data, schema=columns)
        ddf = df.withColumn("salary", col("salary").cast("Double"))
        udf = df.withColumn("salary", col("salary") * 100) #Update The Value of an Existing Column
        udf.show()
        ncol = df.withColumn("CopiedColumn", col("salary") * -1) #Create a column from an existing column
        ncol.show()
        df.withColumn("Country", lit("USA")).show() #Add a New Column using withColumn() with constant value
        print('=============================')
        df.withColumnRenamed("gender", "sex") \
            .show(truncate=False) #rename column names

        














