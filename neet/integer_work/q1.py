# q1.py — Dynamic Programming Languages CA 1 — Question 1 (25%)
# Core Python only.
# Run: python q1.py

members = [
    {"name": "Ana",  "year": 1, "scores": [55, 72, 66], "active": True},
    {"name": "Ben",  "year": 2, "scores": [38, 41],     "active": True},
    {"name": "Chao", "year": 3, "scores": [91, 88, 90], "active": True},
    {"name": "Dina", "year": 2, "scores": [49],         "active": True},
    {"name": "Eoin", "year": 4, "scores": [],           "active": True},
]

def avg_score(member: dict) -> int:
    scores = member.get("scores", [])
    return 0 if not scores else sum(scores) // len(scores)

def add_or_update(members_list: list, name: str, year: int, new_score: int) -> list:
    for m in members_list:
        if m.get("name") == name:
            m.setdefault("scores", []).append(new_score)
            return members_list
    # not found: append new
    members_list.append({"name": name, "year": year, "scores": [new_score], "active": True})
    return members_list

def drop_underperformers(members_list: list, threshold: int) -> None:
    for m in members_list:
        if avg_score(m) < threshold or m.get("year", 0) > 4:
            m["active"] = False

if __name__ == "__main__":
    print("Initial members:")
    for m in members: print(m, "avg:", avg_score(m))
    add_or_update(members, "Ana", 1, 80)
    add_or_update(members, "Zed", 5, 77)  
    print("\nAfter add_or_update:")
    for m in members: print(m, "avg:", avg_score(m))
    drop_underperformers(members, threshold=60)
    print("\nAfter drop_underperformers(threshold=60):")
    for m in members: print(m, "avg:", avg_score(m))
