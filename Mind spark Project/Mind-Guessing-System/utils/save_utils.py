import json, os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_DIR = os.path.dirname(CURRENT_DIR)
PENDING_FILE = os.path.join(MAIN_DIR, "pending_updates.json")

def save_new_entry(category, name, answers, special_feature=None):
    print(" Saving to:", PENDING_FILE)

    new_attrs = [k for k, v in answers.items() if v == "yes"]
    if special_feature:
        new_attrs.append(special_feature)
    new_attrs = list(set(new_attrs))

    suggestion = {
        "category": category,
        "suggested_name": name,
        "suggested_attrs": new_attrs
    }

    
    if os.path.exists(PENDING_FILE):
        try:
            with open(PENDING_FILE, "r", encoding="utf-8") as f:
                data = f.read().strip()
                pending = json.loads(data) if data else []
        except:
            pending = []
    else:
        pending = []

    pending.append(suggestion)

   
    with open(PENDING_FILE, "w", encoding="utf-8") as f:
        json.dump(pending, f, indent=2, ensure_ascii=False)

    print(" Saved successfully!")
