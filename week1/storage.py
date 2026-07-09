import json
from pathlib import Path

DATA_FILE = Path("data/students.json")


def load_students():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_students(students):
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)