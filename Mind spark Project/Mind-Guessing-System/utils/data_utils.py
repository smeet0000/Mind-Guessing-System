import json, os

def load_data(category):
    filename = f"{category}.json"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        for d in data:
            d.setdefault("attrs", [])
        return data
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return []

def filter_candidates(candidates, attr, ans):
    if ans == "yes":
        return [c for c in candidates if attr in c.get("attrs", [])]
    elif ans == "no":
        return [c for c in candidates if attr not in c.get("attrs", [])]
    return candidates
