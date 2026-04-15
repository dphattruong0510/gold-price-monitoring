import json
import os
from typing import Any

def append_to_json(document: dict[str, Any], file_path: str = "data/gold_prices.json") -> None:
    os.makedirs("data", exist_ok=True)

    history = []

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []

    history.append(document)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)