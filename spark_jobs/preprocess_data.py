from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
import time

start = time.time()

spark = SparkSession.builder.appName("ChurnPreprocessing").getOrCreate()

df = spark.read.csv("data/raw/churn_data.csv", header=True, inferSchema=True)
df_cleaned = df.dropna().withColumn("label", when(col("churn") == "Yes", 1).otherwise(0))
df_cleaned.write.mode("overwrite").parquet("data/processed/cleaned_data.parquet")
spark.stop()

print("Time (PySpark):", time.time() - start)
