import os
import csv
import hashlib

from PIL import Image


DATASET_DIR = "data/raw"
REPORT_FILE = "data/processed/cleaning_report.csv"

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def file_hash(file_path):
    """Generate a hash to identify duplicate files."""
    hasher = hashlib.md5()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hasher.update(chunk)

    return hasher.hexdigest()


def clean_dataset():
    records = []
    seen_hashes = set()

    if not os.path.exists(DATASET_DIR):
        print(f"Dataset directory not found: {DATASET_DIR}")
        return

    for root, _, files in os.walk(DATASET_DIR):

        for filename in files:
            file_path = os.path.join(root, filename)

            if not filename.lower().endswith(VALID_EXTENSIONS):
                continue

            status = "valid"
            image_hash = ""

            try:
                with Image.open(file_path) as image:
                    image.verify()

                image_hash = file_hash(file_path)

                if image_hash in seen_hashes:
                    status = "duplicate"
                else:
                    seen_hashes.add(image_hash)

            except Exception:
                status = "invalid"

            records.append({
                "file_name": filename,
                "relative_path": os.path.relpath(file_path, DATASET_DIR),
                "status": status
            })

    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)

    with open(REPORT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["file_name", "relative_path", "status"]
        )

        writer.writeheader()
        writer.writerows(records)

    valid = sum(r["status"] == "valid" for r in records)
    duplicate = sum(r["status"] == "duplicate" for r in records)
    invalid = sum(r["status"] == "invalid" for r in records)

    print("\nDataset Cleaning Report")
    print("-----------------------")
    print(f"Valid images      : {valid}")
    print(f"Duplicate images  : {duplicate}")
    print(f"Invalid images    : {invalid}")
    print(f"Report saved to   : {REPORT_FILE}")


if __name__ == "__main__":
    clean_dataset()