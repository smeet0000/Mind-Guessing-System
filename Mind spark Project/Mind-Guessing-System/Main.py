import json
import random
import os

# category → question map imports
from animal_que import get_questions as animal_questions
from object_que import get_questions as object_questions
from character_que import get_questions as character_questions


# --- Generate a question for a given attribute ---
def make_question(attr, category):
    questions_map = {
        "animals": animal_questions(),
        "objects": object_questions(),
        "characters": character_questions()
    }
    return questions_map[category].get(attr, f"Does it have '{attr}'?")


# --- Load data from main category file ---
def load_data(category):
    filename = f"{category}.json"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# --- Save new or updated data to pending file (NOT main DB) ---
def save_new_entry(category, name, answers, special_feature=None):
    pending_file = "pending_updates.json"

    new_attrs = [attr for attr, ans in answers.items() if ans == "yes"]

    if special_feature:
        new_attrs.append(special_feature)

    new_attrs = list(set(new_attrs))

    suggestion = {
        "category": category,
        "suggested_name": name,
        "suggested_attrs": new_attrs
    }

    if os.path.exists(pending_file):
        with open(pending_file, "r", encoding="utf-8") as f:
            try:
                pending = json.load(f)
            except json.JSONDecodeError:
                pending = []
    else:
        pending = []

    pending.append(suggestion)

    with open(pending_file, "w", encoding="utf-8") as f:
        json.dump(pending, f, indent=2, ensure_ascii=False)

    print("📝 Suggestion saved.")


COMMON_ATTRS_PRIORITY_CHARACTER = [
    "real", "mythological", "animated",
    "male", "female", "child_star", "indian", "international",
    "actor", "bollywood", "hollywood", "tollywood", "gujarati_actor",
    "tv_actor", "ott_actor", "tvf_actor",
    "cricketer", "chess_player", "tennis_player", "boxer", "badminton_player",
    "athlete", "businessperson", "politician", "indian_leader", "historic_icon",
    "monk", "teacher", "mentor", "educator", "podcaster",
    "tall", "fit", "muscular", "intelligent", "brave", "funny",
    "youtuber", "instagram_star", "vlogger", "family_vlogger", "daily_vlogger",
    "gamer", "streamer", "content_creator", "storytelling_videos",
    "creative_scripts", "positive_content", "entertaining",
    "awardee",
    "director", "producer", "writer", "composer", "music_composer",
    "lyricist", "singer", "singer_songwriter", "musician",
    "choreographer", "dancer", "rapper"
]

COMMON_ATTRS_PRIORITY_ANIMAL = [
    "mammal", "bird", "fish", "reptile", "amphibian", "insect", "arachnid", "invertebrate",
    "four_legs", "two_legs","eight_legs", "no_legs",
    "wild", "domestic",
    "social", "solitary", "diurnal", "nocturnal",
    "wings", "tail", "fur", "feathered", "scales",
    "warm_blooded", "cold_blooded",
   
]

# COMMON_ATTRS_PRIORITY_OBJECT = [
#     "furniture", "kitchen_item", "utensil", "appliance", "electronics",
#     "personal_item", "accessory", "bag", "cleaning_item", "bath_item",
#     "clothing", "stationery", "vehicle", "safety_item", "toy_or_sports_item",
#     "sports_item", "camping_item", "tool", "hardware_item", "food",
#     "home_decor", "container"
# ]

COMMON_ATTRS_PRIORITY_OBJECT = [
    "food", "electronics", "vehicle", 
    "household_item", "furniture", "clothing", "accessory", "personal_item", "bag",
    "stationery", "toy", "sports_item",
    "cleaning_item", "kitchen_item", "container",
     "camping_item", "tool",
    "hardware_item", "safety_item"
]


# --- Choose next attribute ---
def pick_next_attribute(candidates, asked, category):
    if category == "animals":
        priority_list = COMMON_ATTRS_PRIORITY_ANIMAL
    elif category == "objects":
        priority_list = COMMON_ATTRS_PRIORITY_OBJECT
    else:
        priority_list = COMMON_ATTRS_PRIORITY_CHARACTER

    for attr in priority_list:
        if attr not in asked and any(attr in c.get("attrs", []) for c in candidates):
            return attr

    attr_counts = {}
    for it in candidates:
        for a in it.get("attrs", []):
            if a not in asked:
                attr_counts[a] = attr_counts.get(a, 0) + 1

    if not attr_counts:
        return None

    total = len(candidates)
    scored = {a: abs((count / total) - 0.5) for a, count in attr_counts.items()}
    return sorted(scored.items(), key=lambda x: x[1])[0][0]


# --- Filter candidates ---
def filter_candidates(candidates, attr, ans):
    if ans == "yes":
        return [c for c in candidates if attr in c.get("attrs", [])]
    elif ans == "no":
        return [c for c in candidates if attr not in c.get("attrs", [])]
    return candidates


# --- Numeric input ---
def ask_numeric_choice(prompt, choices):
    choice_text = "  ".join(f"{k}={v}" for k, v in choices.items())
    while True:
        ans = input(f"{prompt} ({choice_text}) → ").strip()
        if ans.isdigit() and int(ans) in choices:
            return int(ans)
        print("Invalid choice.")


# ==========================================================
#   MAIN ROUND (UPDATED NO EARLY GUESS)
# ==========================================================
def play_one_round():
    print("Choose a category: 1. Animal  2. Character  3. Object")
    cat_choice = input("Enter number: ").strip()

    category = "animals" if cat_choice == "1" else "characters" if cat_choice == "2" else "objects"
    candidates = load_data(category)

    asked = set()
    answers = {}

    MIN_Q = 20
    MAX_Q = 25
    questions_asked = 0

    print(f"\nThink of a {category[:-1]}... I will ask 20–25 questions.")

    while questions_asked < MAX_Q:
        attr = pick_next_attribute(candidates, asked, category)
        if not attr:
            break

        q = make_question(attr, category)
        ans_key = ask_numeric_choice(q, {1: "Yes", 2: "No", 3: "Don't know"})
        ans = {1: "yes", 2: "no", 3: "maybe"}[ans_key]

        asked.add(attr)
        answers[attr] = ans
        candidates = filter_candidates(candidates, attr, ans)

        questions_asked += 1

        # 🚫 REMOVED EARLY GUESS FEATURE
        # No break even if 1 candidate remains

    # ======================================================
    #   FINAL GUESS (AFTER ALL QUESTIONS ONLY)
    # ======================================================
    if candidates:
        guess = random.choice(candidates)["name"]
        ans_key = ask_numeric_choice(
            f"\nMy FINAL guess is: '{guess}'. Is that correct?",
            {1: "Yes", 2: "No"}
        )

        if ans_key == 1:
            print("🎉 Correct! I guessed it!")
            return
        else:
            print("❌ Wrong guess.")
    else:
        print("\nNo matching item found.")

    # ask for correct name
    real = input("Enter the correct name (or press Enter to skip): ").strip()
    if real:
        special = input("Enter special attribute (optional): ").strip()
        save_new_entry(category, real, answers, special if special else None)


# ==========================================================
#  MAIN LOOP
# ==========================================================
def main():
    print("=== Mind Guessing System (NO EARLY GUESS VERSION) ===")
    while True:
        play_one_round()
        again = ask_numeric_choice("\nPlay again?", {1: "Yes", 2: "No"})
        if again != 1:
            break


if __name__ == "__main__":
    main()
