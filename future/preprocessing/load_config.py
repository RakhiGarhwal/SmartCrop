import os
import yaml

CONFIG_FILE = "data/dataset_config.yaml"


def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"Configuration file not found: {CONFIG_FILE}")
        return None

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config


if __name__ == "__main__":
    config = load_config()

    if config:
        print("SmartCrop Dataset Configuration")
        print("--------------------------------")

        datasets = config.get("datasets", {})

        for crop, details in datasets.items():
            print(
                f"{crop:15} | "
                f"Priority: {details['priority']:6} | "
                f"Status: {details['status']}"
            )