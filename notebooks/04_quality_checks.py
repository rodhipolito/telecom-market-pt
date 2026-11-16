# Databricks notebook source
# MAGIC %md
# MAGIC # 04 — Quality checks
# MAGIC Last task of the job. Any failed check raises and stops the run.

# COMMAND ----------

from pyspark.sql import functions as F

def check(name, bad_rows_df, max_rows=0):
    n = bad_rows_df.count()
    assert n <= max_rows, f"QUALITY CHECK FAILED: {name} ({n} bad rows)"
    print(f"OK  {name}")

# COMMAND ----------

gold = spark.table("workspace.telecom.gold_market_share_quarterly")

check("no null operator", gold.filter(F.col("operator").isNull()))
check("share between 0 and 100",
      gold.filter((F.col("market_share_pct") < 0) | (F.col("market_share_pct") > 100)))
check("period sums to ~100",
      gold.groupBy("segment", "period").agg(F.sum("market_share_pct").alias("total"))
          .filter((F.col("total") < 98) | (F.col("total") > 102)))
check("no duplicate keys",
      gold.groupBy("segment", "period", "operator").count().filter(F.col("count") > 1))
