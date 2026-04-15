#!/bin/bash
set -e

echo "=============================="
echo "Gold Price Monitoring Pipeline"
echo "Started at: $(date)"
echo "=============================="

echo ""
echo "[1/6] Scraping and saving raw data..."
python -m sources.scraper.main

echo ""
echo "[2/6] Loading MongoDB data to Supabase with dlt..."
python -m sources.pipeline.dlt_ingestion

echo ""
echo "[3/6] Running dbt models..."
cd dbt_project/gold_dbt
dbt run --profiles-dir .

echo ""
echo "[4/6] Running dbt tests..."
dbt test --profiles-dir .
cd ../..

echo ""
echo "[5/6] Running analysis..."
python -m sources.analytics.analysis

echo ""
echo "[6/6] Generating charts..."
python -m sources.analytics.visualize

echo ""
echo "Finished at: $(date)"
echo "Pipeline completed successfully."