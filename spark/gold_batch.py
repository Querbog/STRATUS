from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg

# --------------------------------------------------
# 1. Create Spark Session (Batch Job)
# --------------------------------------------------
spark = SparkSession.builder \
    .appName("StudentEngagementGoldBatch") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# --------------------------------------------------
# 2. Read Silver Layer Parquet Data
# --------------------------------------------------
silver_df = spark.read.parquet(
    "file:///tmp/silver_student_activity"
)

# --------------------------------------------------
# 3. Basic Cleanup (cast numeric fields)
# --------------------------------------------------
clean_df = silver_df \
    .withColumn("time_spent", col("time_spent").cast("int")) \
    .withColumn("videos_watched", col("videos_watched").cast("int")) \
    .withColumn("quiz_attempts", col("quiz_attempts").cast("int"))

# --------------------------------------------------
# 4. GOLD AGGREGATIONS
# --------------------------------------------------

# 4.1 Engagement distribution
engagement_dist_df = clean_df.groupBy("engagement_level") \
    .agg(
        count("*").alias("total_students"),
        avg("time_spent").alias("avg_time_spent")
    )

# --------------------------------------------------
# 5. Write Gold Layer Output
# --------------------------------------------------
engagement_dist_df.write \
    .mode("overwrite") \
    .parquet("file:///tmp/gold_student_engagement")

# --------------------------------------------------
# 6. Show result (for verification only)
# --------------------------------------------------
engagement_dist_df.show(truncate=False)
