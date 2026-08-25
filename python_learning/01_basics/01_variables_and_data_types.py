"""
Module 1: Variables and Data Types
====================================
Learn how Python handles variables and the core data types.
Use GitHub Copilot: start typing a variable name and let Copilot suggest values and types.
"""

# --- Integers ---
age = 25
year = 2024

# --- Floats ---
temperature = 36.6
pi = 3.14159

# --- Strings ---
name = "Alice"
greeting = f"Hello, {name}! You are {age} years old."

# --- Booleans ---
is_student = True
has_graduated = False

# --- NoneType ---
middle_name = None

# --- Type checking ---
print(type(age))          # <class 'int'>
print(type(temperature))  # <class 'float'>
print(type(name))         # <class 'str'>
print(type(is_student))   # <class 'bool'>
print(type(middle_name))  # <class 'NoneType'>

# --- Type conversion ---
age_as_string = str(age)
temperature_as_int = int(temperature)

print(greeting)
print(f"age as string: '{age_as_string}', temperature as int: {temperature_as_int}")
