import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "db.json")


def load_data():
    if not os.path.exists(DB_PATH):
        return {"high_score": 0}
    with open(DB_PATH, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f)


def save_score(score):
    data = load_data()

    if score > data.get("high_score", 0):
        data["high_score"] = score
        save_data(data)