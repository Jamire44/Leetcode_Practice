# q3.py — Dynamic Programming Languages CA 1 — Question 3 (25%)
# Uses pandas only (as permitted). No other 3rd-party libs.
# Run: python q3.py

import pandas as pd
import json

# --- Part (a): build DataFrame and print basics ---

data = {
    "student": ["Alice","Bob","Cathy","Dan","Eva","Frank","Grace","Hugo"],
    "year":    [1, 2, 2, 3, 1, 3, 2, 1],
    "score":   [85, 46, 79, 58, 93, 67, 52, 88],
    "passed":  [True, False, True, False, True, True, False, True],
}

df = pd.DataFrame(data)

print("DataFrame shape (rows, cols):", df.shape)
print("\nFirst 3 rows:")
print(df.head(3))
print("\nLast 2 rows:")
print(df.tail(2))

print("\nYear==2, only student and score columns:")
print(df.loc[df["year"] == 2, ["student", "score"]])

# --- Part (b): grade column + passed override ---

def grade_from_score(s):
    if s >= 90:
        return "A"
    if 70 <= s < 90:
        return "B"
    return "C"

df["grade"] = df["score"].apply(grade_from_score)
df.loc[df["passed"] == False, "grade"] = "F"

print("\nRows with grade C or F:")
print(df[df["grade"].isin(["C", "F"])])

# --- Part (c): groupby year stats ---
year_stats = df.groupby("year").agg(
    avg_score=("score", "mean"),
    count=("student", "count"),
).reset_index()

print("\nYear stats:")
print(year_stats)

# --- Part (d): JSON parsing & outputs ---

json_str = 