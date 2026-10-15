#!/usr/bin/env python3
"""Summarize a sales CSV and save a Markdown report beside the input file."""

import argparse
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {"Month", "Product", "Units", "UnitPrice", "UnitCost"}
NUMBER_COLUMNS = ("Units", "UnitPrice", "UnitCost")


def build_report(source: Path) -> str:
    """Read and validate the CSV, then return a human-readable report."""
    data = pd.read_csv(source)
    missing = REQUIRED_COLUMNS - set(data.columns)
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(sorted(missing)))
    if data.empty:
        raise ValueError("The CSV contains no data rows.")

    # Fail clearly on text or negative quantities/prices/costs.
    for column in NUMBER_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="raise")
    if (data[list(NUMBER_COLUMNS)] < 0).any().any():
        raise ValueError("Units, prices, and costs must not be negative.")

    data["Revenue"] = data["Units"] * data["UnitPrice"]
    data["Cost"] = data["Units"] * data["UnitCost"]
    data["GrossProfit"] = data["Revenue"] - data["Cost"]
    monthly = data.groupby("Month", sort=False)[["Revenue", "Cost", "GrossProfit"]].sum()
    products = data.groupby("Product", sort=False)[["Units", "Revenue", "Cost", "GrossProfit"]].sum()
    totals = data[["Revenue", "Cost", "GrossProfit"]].sum()
    margin = totals["GrossProfit"] / totals["Revenue"] * 100 if totals["Revenue"] else 0

    lines = [
        "# Business Sales Analysis", "", f"Source: `{source.name}`",
        f"Rows analyzed: {len(data)}", "", "## Summary",
        f"- Total revenue: {totals['Revenue']:,.2f}",
        f"- Total cost: {totals['Cost']:,.2f}",
        f"- Gross profit: {totals['GrossProfit']:,.2f}",
        f"- Gross margin: {margin:.2f}%", "", "## Monthly performance", "",
        "| Month | Revenue | Cost | Gross profit |", "|---|---:|---:|---:|",
    ]
    for month, row in monthly.iterrows():
        lines.append(f"| {month} | {row['Revenue']:,.2f} | {row['Cost']:,.2f} | {row['GrossProfit']:,.2f} |")

    lines.extend([
        "", "## Product performance", "",
        "| Product | Units | Revenue | Cost | Gross profit |",
        "|---|---:|---:|---:|---:|",
    ])
    for product, row in products.iterrows():
        lines.append(
            f"| {product} | {row['Units']:,.0f} | {row['Revenue']:,.2f} | "
            f"{row['Cost']:,.2f} | {row['GrossProfit']:,.2f} |"
        )
    lines.extend([
        "", "## Limitations", "",
        "- Currency is not specified.",
        "- Gross profit excludes expenses not represented by `UnitCost`.",
        "- Validate the input data and account for relevant expenses before making decisions.",
        "- This report describes the supplied rows; it is not business advice.", "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path, help="CSV containing Month, Product, Units, UnitPrice, UnitCost")
    parser.add_argument(
        "--output", type=Path,
        help="report path (default: business-analysis-report.md beside the CSV)",
    )
    args = parser.parse_args()
    source = args.csv_file.expanduser().resolve()
    if not source.is_file():
        parser.error(f"CSV file not found: {source}")

    destination = args.output.expanduser().resolve() if args.output else source.parent / "business-analysis-report.md"
    try:
        report = build_report(source)
    except (ValueError, OSError, pd.errors.ParserError) as error:
        parser.error(str(error))

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(report, encoding="utf-8")
    print(f"Report saved to: {destination}")


if __name__ == "__main__":
    main()
