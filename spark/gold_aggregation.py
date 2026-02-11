from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    countDistinct,
    sum,
    col
)

# ----------------------------------------
# 1. Create Spark Session
# ----------------------------------------
spark = SparkSession.builder \
    .appName("StudentActivityGoldAggregation") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ----------------------------------------
# 2. Read Silver Structured Data (BATCH)
# ----------------------------------------
silver_df = spark.read.parquet(
    "file:///home/talentum/student_streaming_project/data/silver_structured"
)

# ----------------------------------------
# 3. Gold Aggregations
# ----------------------------------------
gold_df = silver_df.groupBy("CourseCategory").agg(
    countDistinct("UserID").alias("total_users"),
    avg("TimeSpentOnCourse").alias("avg_time_spent"),
    avg("QuizScores").alias("avg_quiz_score"),
    avg("CompletionRate").alias("avg_completion_rate"),
    sum(col("CourseCompletion")).alias("completed_users")
)

# ----------------------------------------
# 4. Completion Ratio
# ----------------------------------------
gold_df = gold_df.withColumn(
    "completion_ratio",
    col("completed_users") / col("total_users")
)

# ----------------------------------------
# 5. Write Gold Data
# ----------------------------------------
gold_df.write.mode("overwrite").parquet(
    "file:///home/talentum/student_streaming_project/data/gold"
)

print("✅ Gold layer successfully created")

spark.stop()

