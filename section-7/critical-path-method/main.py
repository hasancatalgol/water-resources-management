#!/usr/bin/env python3
# deps: pycritical, pandas, openpyxl

from pathlib import Path
import pandas as pd
from pyCritical.src import critical_path_method, gantt_chart  # <- case-sensitive!

EXCEL_PATH = Path("section-7/critical-path-method/cpm_tasks.xlsx")
SHEET_NAME = "example"   # <-- your sheet name

def load_dataset():
    # columns must be: job | predecessors | time
    df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME,
                       dtype={"job": str, "predecessors": str, "time": float})
    # treat "-", "—", or NaN as no predecessors
    df["predecessors"] = df["predecessors"].fillna("").replace({"-": "", "—": ""})
    dataset = []
    for _, r in df.iterrows():
        job = r["job"].strip()
        preds = [p.strip() for p in r["predecessors"].split(",") if p.strip()]
        dur = float(r["time"])
        dataset.append([job, preds, dur])
    return dataset

def main():
    if not EXCEL_PATH.exists():
        raise SystemExit(f"Excel not found: {EXCEL_PATH}")
    dataset = load_dataset()
    cpm = critical_path_method(dataset)
    print("\nCPM results:\n", cpm)
    gantt_chart(dataset, cpm, size_x=15, size_y=7, show_slack=True)

if __name__ == "__main__":
    main()
