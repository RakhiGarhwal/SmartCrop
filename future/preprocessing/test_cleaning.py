import os
from PIL import Image

import clean_dataset


TEST_DIR = "data/raw/cleaning_test"


def create_test_dataset():
    os.makedirs(TEST_DIR, exist_ok=True)

    # 1. Valid image
    Image.new("RGB", (224, 224), "white").save(
        os.path.join(TEST_DIR, "valid_image.jpg")
    )

    # 2. Exact duplicate of the valid image
    Image.new("RGB", (224, 224), "white").save(
        os.path.join(TEST_DIR, "duplicate_image.jpg")
    )

    # 3. Invalid/corrupt image
    with open(os.path.join(TEST_DIR, "corrupt_image.jpg"), "w") as file:
        file.write("This is not a real image.")


def test_cleaning():
    create_test_dataset()

    clean_dataset.DATASET_DIR = TEST_DIR
    clean_dataset.REPORT_FILE = "data/processed/cleaning_test_report.csv"

    clean_dataset.clean_dataset()


if __name__ == "__main__":
    test_cleaning()