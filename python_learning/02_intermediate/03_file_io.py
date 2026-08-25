"""
Module 7: File I/O
====================
Reading from and writing to files in Python.
Copilot tip: describe the file operation in a comment — Copilot handles the boilerplate.
"""

import json
import os
import tempfile


# ---------- Write and read a plain text file ----------
def demo_text_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tmp:
        path = tmp.name
        lines = ["Line 1: Hello, Python!\n", "Line 2: Learning file I/O.\n", "Line 3: Done.\n"]
        tmp.writelines(lines)

    print("--- Reading text file ---")
    with open(path) as fh:
        for line in fh:
            print(line, end="")

    os.unlink(path)


# ---------- Write and read a JSON file ----------
def demo_json_file():
    data = {
        "name": "Eve",
        "skills": ["Python", "GitHub Copilot", "Data Analysis"],
        "experience_years": 3,
    }

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
        path = tmp.name
        json.dump(data, tmp, indent=2)

    print("\n--- Reading JSON file ---")
    with open(path) as fh:
        loaded = json.load(fh)

    print(f"Name: {loaded['name']}")
    print(f"Skills: {', '.join(loaded['skills'])}")
    print(f"Experience: {loaded['experience_years']} years")

    os.unlink(path)


# ---------- Appending to a file ----------
def demo_append():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as tmp:
        path = tmp.name
        tmp.write("First entry.\n")

    with open(path, "a") as fh:
        fh.write("Second entry.\n")
        fh.write("Third entry.\n")

    print("\n--- Reading appended log ---")
    with open(path) as fh:
        print(fh.read())

    os.unlink(path)


if __name__ == "__main__":
    demo_text_file()
    demo_json_file()
    demo_append()
