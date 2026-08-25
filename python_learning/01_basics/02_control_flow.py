"""
Module 2: Control Flow
========================
Learn how to use if/elif/else, for loops, and while loops.
Tip: Describe what you want in a comment and let Copilot generate the logic.
"""

# --- if / elif / else ---
score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")

# --- for loop over a list ---
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# --- for loop with range ---
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# --- while loop ---
count = 0
while count < 3:
    print(f"count is {count}")
    count += 1

# --- loop control: break and continue ---
print("\nSkipping even numbers up to 10:")
for n in range(1, 11):
    if n % 2 == 0:
        continue
    if n > 7:
        break
    print(n)
