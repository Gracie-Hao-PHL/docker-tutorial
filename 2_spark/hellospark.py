from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType


def main():
    # Spark session & context
    spark = SparkSession.builder.getOrCreate()

    _data = [
        ("James","","Smith","36636","M",3000),
        ("Michael","Rose","","40288","M",4000),
        ("Robert","","Williams","42114","M",4000),
        ("Maria","Anne","Jones","39192","F",4000),
        ("Jen","Mary","Brown","","F",-1)
    ]

    schema = StructType([ \
        StructField("firstname",StringType(),True),
        StructField("middlename",StringType(),True),
        StructField("lastname",StringType(),True),
        StructField("id", StringType(), True),
        StructField("gender", StringType(), True),
        StructField("salary", IntegerType(), True)
    ])
    
    df = spark.createDataFrame(data=_data,schema=schema)
    df.printSchema()
    df.show(truncate=False)

    breakpoint()

    df.write.csv('output_default_partitions')
    df.repartition(2).write.csv('output_2_partitions'
    )

if __name__=='__main__':
    main()