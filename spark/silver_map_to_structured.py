from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SilverMapToStructured") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# --------------------------------------------------
# 1. Read Silver (MapType)
# --------------------------------------------------
silver_df = spark.read.parquet(
    "file:///home/talentum/student_streaming_project/data/silver"
)

# --------------------------------------------------
# 2. Extract & cast fields safely from map
# --------------------------------------------------
structured_df = silver_df.select(
    col("data")["UserID"].cast("int").alias("UserID"),
    col("data")["CourseCategory"].alias("CourseCategory"),
    col("data")["TimeSpentOnCourse"].cast("double").alias("TimeSpentOnCourse"),
    col("data")["NumberOfVideosWatched"].cast("int").alias("NumberOfVideosWatched"),
    col("data")["NumberOfQuizzesTaken"].cast("int").alias("NumberOfQuizzesTaken"),
    col("data")["QuizScores"].cast("double").alias("QuizScores"),
    col("data")["CompletionRate"].cast("double").alias("CompletionRate"),
    col("data")["DeviceType"].cast("int").alias("DeviceType"),
    col("data")["CourseCompletion"].cast("int").alias("CourseCompletion"),
    col("data")["event_time"].alias("event_time")
)

# --------------------------------------------------
# 3. Write structured Silver
# --------------------------------------------------
structured_df.write.mode("overwrite").parquet(
    "file:///home/talentum/student_streaming_project/data/silver_structured"
)

print("✅ Structured Silver created successfully")

