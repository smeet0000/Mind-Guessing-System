from animal_que import get_questions as animal_questions
from object_que import get_questions as object_questions
from character_que import get_questions as character_questions
from priorities import (
    COMMON_ATTRS_PRIORITY_ANIMAL,
    COMMON_ATTRS_PRIORITY_OBJECT,
    COMMON_ATTRS_PRIORITY_CHARACTER
)


def make_question(attr, category):
    maps = {
        "animals": animal_questions(),
        "objects": object_questions(),
        "characters": character_questions()
    }
    return maps.get(category, {}).get(attr, f"Does it '{attr}'?")


def get_priority_list(category):
    """Return the correct priority attribute list for the given category."""
    return {
        "animals": COMMON_ATTRS_PRIORITY_ANIMAL,
        "objects": COMMON_ATTRS_PRIORITY_OBJECT,
        "characters": COMMON_ATTRS_PRIORITY_CHARACTER
    }.get(category, [])


def pick_next_attribute(candidates, asked, category, priority_list=None):
    # Pick the next best attribute based on priority or balanced info gain.
    if not priority_list:
        priority_list = get_priority_list(category)

    for attr in priority_list:
        if attr not in asked and any(attr in c.get("attrs", []) for c in candidates):
            return attr

  
    attr_counts = {}
    for c in candidates:
        for a in c.get("attrs", []):
            if a not in asked:
                attr_counts[a] = attr_counts.get(a, 0) + 1

    if not attr_counts:
        return None

    total = len(candidates)
    scored_attrs = {a: abs((count / total) - 0.5) for a, count in attr_counts.items()}
    sorted_attrs = sorted(scored_attrs.items(), key=lambda x: x[1])
    return sorted_attrs[0][0] if sorted_attrs else None
