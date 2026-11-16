# Databricks notebook source
# MAGIC %md
# MAGIC # 02 — Silver
# MAGIC Typed columns, clean names, deduplicated. Week 3 replaces overwrite with MERGE.
# MAGIC
# MAGIC Reads: bronze tables · Writes: `silver_mobile_share`, `silver_fixed_internet_share`

# COMMAND ----------

from pyspark.sql import functions as F

df = spark.table("workspace.telecom.bronze_mobile_share")
df.printSchema()
display(df.describe())

# COMMAND ----------

# TODO week 2: replace column names below with the real ones from printSchema()
silver_mobile = (df
    .withColumnRenamed("Operador", "operator")
    .withColumn("period", F.to_date(F.col("Periodo"), "yyyy-MM"))
    .withColumn("market_share_pct",
                F.regexp_replace(F.col("Valor"), ",", ".").cast("double"))
    .select("period", "operator", "market_share_pct")
    .dropDuplicates()
    .filter(F.col("market_share_pct").isNotNull()))

display(silver_mobile)

# COMMAND ----------

silver_mobile.write.mode("overwrite").saveAsTable("workspace.telecom.silver_mobile_share")

# COMMAND ----------

# TODO week 2: repeat for bronze_fixed_internet_share -> silver_fixed_internet_share
