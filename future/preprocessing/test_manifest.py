import os
import shutil
from PIL import Image

import create_manifest


TEST_DIR = "data/raw/test_dataset"


def create_test_images():
    os.makedirs(TEST_DIR, exist_ok=True)

    Image.new("RGB", (224, 224), "white").save(
        os.path.join(TEST_DIR, "wheat_healthy.jpg")
    )

    Image.new("RGB", (256, 256), "green").save(
        os.path.join(TEST_DIR, "rice_disease.png")
    )

    Image.new("RGB", (128, 128), "yellow").save(
        os.path.join(TEST_DIR, "maize_leaf.jpg")
    )


def test_manifest():
    create_test_images()

    create_manifest.DATASET_DIR = TEST_DIR
    create_manifest.OUTPUT_FILE = "data/processed/test_manifest.csv"

    create_manifest.create_manifest()

    assert os.path.exists(create_manifest.OUTPUT_FILE)

    print("Manifest test completed successfully!")


if __name__ == "__main__":
    test_manifest()