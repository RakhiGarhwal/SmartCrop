import os
from PIL import Image

DATASET_DIR = "data/raw"

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def validate_dataset():
    total_files = 0
    valid_images = 0
    invalid_images = 0
    unsupported_files = 0

    if not os.path.exists(DATASET_DIR):
        print(f"Dataset directory not found: {DATASET_DIR}")
        return

    for root, _, files in os.walk(DATASET_DIR):
        for filename in files:
            total_files += 1
            file_path = os.path.join(root, filename)

            if not filename.lower().endswith(VALID_EXTENSIONS):
                unsupported_files += 1
                print(f"Unsupported file: {file_path}")
                continue

            try:
                with Image.open(file_path) as img:
                    img.verify()

                valid_images += 1

            except Exception:
                invalid_images += 1
                print(f"Invalid/corrupt image: {file_path}")

    print("\nDataset Validation Report")
    print("-------------------------")
    print(f"Total files       : {total_files}")
    print(f"Valid images      : {valid_images}")
    print(f"Invalid images    : {invalid_images}")
    print(f"Unsupported files : {unsupported_files}")


if __name__ == "__main__":
    validate_dataset()