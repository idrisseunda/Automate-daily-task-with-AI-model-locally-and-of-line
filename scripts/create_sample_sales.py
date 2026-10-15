#!/usr/bin/env python3
"""Create the fictional CSV used by the business-analysis demo."""

import argparse
from pathlib import Path


SAMPLE_CSV = """Month,Product,Units,UnitPrice,UnitCost
January,Product A,100,10,6
January,Product B,50,20,12
February,Product A,120,10,6
February,Product B,45,20,12
March,Product A,150,10,6
March,Product B,60,20,12
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--directory", type=Path, default=Path("demo-workspace"),
        help="directory for the sample file (default: ./demo-workspace)",
    )
    args = parser.parse_args()
    folder = args.directory.expanduser().resolve()
    folder.mkdir(parents=True, exist_ok=True)
    sample = folder / "sample_sales.csv"
    sample.write_text(SAMPLE_CSV, encoding="utf-8")
    print(f"Created fictional sample data: {sample}")
    print("This script only writes sample_sales.csv in the selected directory.")


if __name__ == "__main__":
    main()
