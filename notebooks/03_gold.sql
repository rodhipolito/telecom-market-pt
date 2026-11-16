-- Databricks notebook source
-- MAGIC %md
-- MAGIC # 03 — Gold
-- MAGIC Business tables: share change per operator, rank per period, leader gap.
-- MAGIC
-- MAGIC Reads: silver tables · Writes: `gold_market_share_quarterly`, `gold_leader_by_period`

-- COMMAND ----------

CREATE OR REPLACE TABLE workspace.telecom.gold_market_share_quarterly AS
SELECT
  'mobile' AS segment,
  period,
  operator,
  market_share_pct,
  market_share_pct - LAG(market_share_pct) OVER (PARTITION BY operator ORDER BY period) AS share_change_pp,
  RANK() OVER (PARTITION BY period ORDER BY market_share_pct DESC) AS rank_in_period
FROM workspace.telecom.silver_mobile_share
UNION ALL
SELECT
  'fixed_internet', period, operator, market_share_pct,
  market_share_pct - LAG(market_share_pct) OVER (PARTITION BY operator ORDER BY period),
  RANK() OVER (PARTITION BY period ORDER BY market_share_pct DESC)
FROM workspace.telecom.silver_fixed_internet_share;

-- COMMAND ----------

-- TODO week 3: gold_leader_by_period (leader per segment/period and gap to second)

-- COMMAND ----------

-- Validation: totals per period should be close to 100
SELECT segment, period, ROUND(SUM(market_share_pct), 2) AS total
FROM workspace.telecom.gold_market_share_quarterly
GROUP BY segment, period
ORDER BY segment, period;
