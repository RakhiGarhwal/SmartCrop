import csv
import os
from collections import Counter

MANIFEST_FILE = "data/processed/dataset_manifest.csv"


def generate_statistics():
    if not os.path.exists(MANIFEST_FILE):
        print(f"Manifest not found: {MANIFEST_FILE}")
        print("Run create_manifest.py after placing a dataset in data/raw.")
        return

    records = []

    with open(MANIFEST_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    if not records:
        print("Manifest is empty.")
        return

    formats = Counter(row["format"] for row in records)

    widths = [int(row["width"]) for row in records]
    heights = [int(row["height"]) for row in records]

    print("\nDataset Statistics")
    print("------------------")
    print(f"Total images : {len(records)}")
    print(f"Image formats: {dict(formats)}")
    print(f"Minimum width: {min(widths)}")
    print(f"Maximum width: {max(widths)}")
    print(f"Minimum height: {min(heights)}")
    print(f"Maximum height: {max(heights)}")


if __name__ == "__main__":
    generate_statistics()