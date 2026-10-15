# Demo 03 — Calculate sales results with Python, then ask AI to explain

**Goal:** calculate totals with deterministic Python and pandas, then ask a local model to describe the report without inventing missing context.

## Before you begin

From the repository root, install project Python dependencies as described in the [README](../../README.md). Start an Ollama model or use the connected model in Open WebUI.

## Step 1: Create the fictional sample CSV

Run:

```bash
python scripts/create_sample_sales.py --directory ~/local-ai-guide-sales-demo
```

This creates `sample_sales.csv` in the named directory. It contains fictional monthly sales and cost data.

## Step 2: Run the analysis

```bash
python analyze_sales.py ~/local-ai-guide-sales-demo/sample_sales.csv
```

The script prints the report path and writes `business-analysis-report.md` beside the CSV. It reads the CSV and does not change it. You can write the report somewhere else with `--output /path/to/report.md`.

Expected summary totals for the sample are revenue **6,800.00**, cost **4,080.00**, and gross profit **2,720.00**. Currency is unspecified.

## Step 3: Ask the local model to explain the report

Open the generated Markdown report and paste it into a chat with the local model, or upload it in Open WebUI. Ask:

```text
Using only this report, explain the revenue, cost, gross profit, and gross margin.
Describe the monthly and product trends. Separate observations supported by the data
from recommendations. Do not invent a currency, expenses, or business context that
the report does not provide.
```

## Step 4: Verify

Compare each figure in the model's answer to the report. Check the source CSV for duplicates, missing values, totals rows, stale spreadsheet values, and costs that are not represented by `UnitCost`.

## Expected result and limitation

Python calculates the figures; the model explains the generated report. The data is fictional and gross profit excludes unlisted expenses, taxes, and overheads. Do not treat this sample as business advice.
