import json
import os

DATA_FILE = "data/inventory.json"


def ensure_data_file():
    """Create the data directory and file if they don't exist."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)


def load_data() -> list[dict]:
    """Load all product records from the JSON file."""
    ensure_data_file()
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data: list[dict]):
    """Save all product records to the JSON file."""
    ensure_data_file()
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
