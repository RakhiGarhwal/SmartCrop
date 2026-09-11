import os
import csv
from PIL import Image

# Change this path when working with an actual dataset
DATASET_DIR = "data/raw"
OUTPUT_FILE = "data/processed/dataset_manifest.csv"

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def create_manifest():
    records = []

    if not os.path.exists(DATASET_DIR):
        print(f"Dataset directory not found: {DATASET_DIR}")
        print("Place the dataset inside data/raw and run again.")
        return

    for root, _, files in os.walk(DATASET_DIR):
        for filename in files:

            if not filename.lower().endswith(VALID_EXTENSIONS):
                continue

            file_path = os.path.join(root, filename)

            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                    image_format = img.format

                relative_path = os.path.relpath(file_path, DATASET_DIR)

                records.append({
                    "file_name": filename,
                    "relative_path": relative_path,
                    "width": width,
                    "height": height,
                    "format": image_format
                })

            except Exception as e:
                print(f"Invalid image skipped: {file_path} ({e})")

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "file_name",
                "relative_path",
                "width",
                "height",
                "format"
            ]
        )

        writer.writeheader()
        writer.writerows(records)

    print(f"Manifest created: {OUTPUT_FILE}")
    print(f"Valid images found: {len(records)}")


if __name__ == "__main__":
    create_manifest()