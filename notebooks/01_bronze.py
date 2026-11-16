# Databricks notebook source
# MAGIC %md
# MAGIC # 01 — Bronze
# MAGIC Loads the raw ANACOM CSVs from the `raw` volume into Delta tables, as-is.
# MAGIC
# MAGIC Reads: `/Volumes/workspace/telecom/raw/*.csv`
# MAGIC Writes: `workspace.telecom.bronze_mobile_share`, `workspace.telecom.bronze_fixed_internet_share`

# COMMAND ----------

dbutils.widgets.text("raw_path", "/Volumes/workspace/telecom/raw")
raw_path = dbutils.widgets.get("raw_path")

# COMMAND ----------

def read_anacom_csv(path):
    # If columns come merged into one, change sep to ","
    # If accents look broken, add .option("encoding", "ISO-8859-1")
    return (spark.read
            .option("header", True)
            .option("sep", ";")
            .csv(path))

# COMMAND ----------

df_mobile = read_anacom_csv(f"{raw_path}/IndI_P070.csv")
display(df_mobile)

# COMMAND ----------

df_mobile.write.mode("overwrite").saveAsTable("workspace.telecom.bronze_mobile_share")

# COMMAND ----------

df_fixed = read_anacom_csv(f"{raw_path}/IndI_P041.csv")
display(df_fixed)

# COMMAND ----------

df_fixed.write.mode("overwrite").saveAsTable("workspace.telecom.bronze_fixed_internet_share")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 'mobile' AS t, COUNT(*) AS rows FROM workspace.telecom.bronze_mobile_share
# MAGIC UNION ALL
# MAGIC SELECT 'fixed', COUNT(*) FROM workspace.telecom.bronze_fixed_internet_share
