from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import MapType, StringType

spark = SparkSession.builder \
    .appName("StudentActivitySilverStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Read from Kafka
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "student_activity") \
    .option("startingOffsets", "earliest") \
    .option("failOnDataLoss", "false") \
    .load()

# Extract message value
value_df = kafka_df.selectExpr(
    "CAST(value AS STRING) as message_value"
)

# Parse JSON as MAP
parsed_df = value_df.select(
    from_json(
        col("message_value"),
        MapType(StringType(), StringType())
    ).alias("data")
)

# Write to Silver (NO trigger)
query = parsed_df.writeStream \
    .format("parquet") \
    .option(
        "path",
        "file:///home/talentum/student_streaming_project/data/silver"
    ) \
    .option(
        "checkpointLocation",
        "file:///home/talentum/student_streaming_project/data/checkpoints/student_activity"
    ) \
    .outputMode("append") \
    .start()

query.awaitTermination()

