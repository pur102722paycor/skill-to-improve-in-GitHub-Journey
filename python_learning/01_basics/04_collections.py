"""
Module 4: Lists, Tuples, Sets, and Dictionaries
================================================
Core Python collection types with practical examples.
Copilot tip: type `# create a list of ...` and let Copilot fill in the rest.
"""

# ---------- Lists ----------
# Ordered, mutable sequences
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.append(7)
numbers.sort()
print("Sorted list:", numbers)
print("First:", numbers[0], "Last:", numbers[-1])

# List comprehension
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

# ---------- Tuples ----------
# Ordered, immutable sequences
coordinates = (10.5, 20.3)
x, y = coordinates          # unpacking
print(f"x={x}, y={y}")

# ---------- Sets ----------
# Unordered collections of unique items
tags = {"python", "github", "copilot", "python"}  # duplicate removed
tags.add("ai")
print("Tags:", tags)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)

# ---------- Dictionaries ----------
# Key-value mappings
person = {
    "name": "Diana",
    "age": 28,
    "skills": ["Python", "SQL", "Git"],
}

print("\nPerson:", person["name"])
person["city"] = "Austin"           # add new key
print("City:", person.get("city"))
print("Keys:", list(person.keys()))

# Dictionary comprehension
word = "hello"
char_count = {ch: word.count(ch) for ch in set(word)}
print("Char count:", char_count)
