# q2.py — Dynamic Programming Languages CA 1 — Question 2 (25%)
# Core Python only. No external libs.
# Run: python q2.py
#
# Expects 'alice.txt' to be in the same directory or provide the absolute path.

import os
import re
from pathlib import Path

# Locate alice.txt (assumes same folder as this script by default)
HERE = Path(__file__).resolve().parent
default_path = HERE / "alice.txt"
ALICE_PATH = Path(os.environ.get("ALICE_TXT", default_path))

def load_lines(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    # Split into lines and strip trailing newlines (no loops needed for stripping at split)
    lines = text.splitlines()
    return text, lines

def remove_gutenberg_header_footer(lines):
    # Find indices of the START/END markers
    start_idx = next((i for i, line in enumerate(lines) if "*** START OF THE PROJECT GUTENBERG EBOOK" in line), None)
    end_idx   = next((i for i, line in enumerate(lines) if "*** END OF THE PROJECT GUTENBERG EBOOK" in line), None)
    # Make book_lines start AFTER START line and end BEFORE END line
    if start_idx is None: start_idx = -1
    if end_idx   is None: end_idx   = len(lines)
    book_lines = lines[start_idx+1:end_idx]  # slicing, no loops
    return book_lines, start_idx, end_idx

def normalise_and_tokenise(book_lines):
    # Join -> single string
    book_text = "\n".join(book_lines)
    # Lowercase
    book_text = book_text.lower()

    # Replace specified punctuation with spaces
    # Characters to remove: . , ; : ! ? ’ ” ( ) [ ] — - *
    # Handle both ascii and unicode quotes/dashes
    punct = r"""[\.\,\;\:\!\?\'\"\(\)\[\]\-\—\*]"""
    book_text = re.sub(punct, " ", book_text)

    # Collapse whitespace to single spaces
    book_text = re.sub(r"\s+", " ", book_text).strip()

    # Split into word list
    words = book_text.split(" ")
    return book_text, words

def print_context(words, idx, window=5):
    # Guard against edges
    left = max(0, idx - window)
    right = min(len(words), idx + window + 1)
    context = words[left:right]
    print(f"Context (idx={idx}):", " ".join(context))

def main():
    print(f"Reading: {ALICE_PATH}")
    text, lines = load_lines(ALICE_PATH)

    # (a) counts and slices
    print("Total number of lines:", len(lines))
    print("\nFirst 3 lines:")
    print("\n".join(lines[:3]))
    print("\nLast 3 lines:")
    print("\n".join(lines[-3:]))

    # (b) remove Project Gutenberg header/footer
    book_lines, start_idx, end_idx = remove_gutenberg_header_footer(lines)
    print(f"\nSTART index: {start_idx}, END index: {end_idx}")
    if len(book_lines) >= 10:
        print("10th line of book_lines:", book_lines[9])
    else:
        print("book_lines shorter than 10 lines.")

    # (c) words processing
    book_text, words = normalise_and_tokenise(book_lines)

    # Prints
    if words:
        print("\nFirst word:", words[0])
    else:
        print("\nNo words found.")
    print("Words [10..19]:", words[10:20])
    print("Last 15 words:", words[-15:])
    print("Every 7th word among first 200:", words[:200:7])

    # (d) first occurrence of 'rabbit' and context window
    try:
        idx = words.index("rabbit")
        print("\nFirst index of 'rabbit':", idx)
        print_context(words, idx, window=5)
    except ValueError:
        print("\n'rabbit' not found in words.")

if __name__ == "__main__":
    main()
