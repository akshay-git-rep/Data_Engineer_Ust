# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

spark = SparkSession.builder \
    .appName("E-commerce Data Analysis") \
    .getOrCreate()


df = spark.read.csv("/FileStore/tables/processed_data.csv", header=True, inferSchema=True)

#remove null
df_cleaned = df.dropna()

# Calculate total sales per category
df_cleaned = df_cleaned.withColumn("Total_Sales", col("Product Price") * col("Quantity Sold"))
total_sales_per_category = df_cleaned.groupBy("Product Category").agg(_sum("Total Sales").alias("Total Sales"))

# total sales per customer
customer_segmentation = df_cleaned.groupBy("Customer ID").agg(_sum("Total Sales").alias("Total Sales"))

# file storing
total_sales_per_category.write.csv("/FileStore/tables/total_sales_per_category.csv", header=True)
customer_segmentation.write.csv("/FileStore/tables/customer_segmentation.csv", header=True)


spark.stop()

