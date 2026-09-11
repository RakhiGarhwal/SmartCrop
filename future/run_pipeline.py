import subprocess
import sys


SCRIPTS = [
    "preprocessing/validate_dataset.py",
    "preprocessing/clean_dataset.py",
    "preprocessing/create_manifest.py",
    "preprocessing/dataset_statistics.py",
]


def run_pipeline():
    print("\n=== SmartCrop Data Preprocessing Pipeline ===\n")

    for script in SCRIPTS:
        print(f"\nRunning: {script}")
        print("-" * 50)

        result = subprocess.run(
            [sys.executable, f"future/{script}"],
            capture_output=True,
            text=True
        )

        if result.stdout:
            print(result.stdout)

        if result.returncode != 0:
            print(f"Pipeline step failed: {script}")

    print("\n=== Pipeline execution completed ===")


if __name__ == "__main__":
    run_pipeline()