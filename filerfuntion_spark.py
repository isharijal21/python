"""function is used to filter the rows from RDD/DataFrame based on the given condition or SQL expression,
 you can also use where() clause instead of the filter() if you are coming from an SQL background,"
 " both these functions operate exactly the same."""
from pyspark.sql.functions import col
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType, IntegerType, ArrayType
from pyspark.sql.functions import array_contains

if __name__ == "__main__":

        spark: SparkSession = SparkSession.builder.master("local[1]").appName("bootcamp.com").getOrCreate()

        data = [
            (("James", "", "Smith"), ["Java", "Scala", "C++"], "OH", "M"),
            (("Anna", "Rose", ""), ["Spark", "Java", "C++"], "NY", "F"),
            (("Julia", "", "Williams"), ["CSharp", "VB"], "OH", "F"),
            (("Maria", "Anne", "Jones"), ["CSharp", "VB"], "NY", "M"),
            (("Jen", "Mary", "Brown"), ["CSharp", "VB"], "NY", "M"),
            (("Mike", "Mary", "Williams"), ["Python", "VB"], "OH", "M")
        ]
        schema = StructType([
            StructField('name', StructType([
                StructField('firstname', StringType(), True),
                StructField('middlename', StringType(), True),
                StructField('lastname', StringType(), True)
            ])),
            StructField('languages', ArrayType(StringType()), True),
            StructField('state', StringType(), True),
            StructField('gender', StringType(), True)
        ])

        df = spark.createDataFrame(data=data, schema=schema)
        df.printSchema()
        df.show(truncate=False)


        #DataFrame filter() with Column Condition
        df.filter(df.state == "OH").show(truncate=False)
        # not equals condition

        df.filter(df.state != "OH") \
            .show(truncate=False)

        df.filter(~(df.state == "OH")) \
            .show(truncate=False)

        df.filter(col("state") == "OH") \
            .show(truncate=False)           #can also be written as

        #DataFrame filter() with SQL Expression

        df.filter("gender == 'M'").show()

        # For not equal
        df.filter("gender != 'M'").show()

        df.filter("gender <> 'M'").show()
        print ("======================")
        #Filter multiple condition
        df.filter((df.state == "OH") & (df.gender == "M")) \
            .show(truncate=False)

        print("======================")

        li = ["OH", "CA", "DE"]
        df.filter(df.state.isin(li)).show() #Filter Based on List Values

        # Filter NOT IS IN List values
        # These show all records with NY (NY is not part of the list)
        df.filter(~df.state.isin(li)).show()
        df.filter(df.state.isin(li) == False).show()
        print("======================")
        #filter Based on Starts With, Ends With, Contains
        # Using startswith
        df.filter(df.state.startswith("N")).show()
        # using endswith
        df.filter(df.state.endswith("H")).show()

        # contains
        df.filter(df.state.contains("H")).show()

        #filter like and rlike
        data2 = [(2, "Michael Rose"), (3, "Robert Williams"),
                 (4, "Rames Rose"), (5, "Rames rose")
                 ]
        df2 = spark.createDataFrame(data=data2, schema=["id", "name"])

        # like - SQL LIKE pattern
        df2.filter(df2.name.like("%rose%")).show()
        #filter on a Array column

        df.filter(array_contains(df.languages, "Java")) \
            .show(truncate=False)
        print("===========================")
        #Struct condition
        df.filter(df.name.lastname == "Williams") \
            .show(truncate=False)





















