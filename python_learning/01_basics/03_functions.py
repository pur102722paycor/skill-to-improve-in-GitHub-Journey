"""
Module 3: Functions
=====================
Learn how to define and use functions in Python.
Copilot tip: Write a docstring first and Copilot will often suggest the full implementation.
"""


# --- Basic function ---
def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


# --- Function with default parameter ---
def power(base, exponent=2):
    """Return base raised to exponent (default: square)."""
    return base ** exponent


# --- Function with multiple return values ---
def min_max(numbers):
    """Return the minimum and maximum values from a list."""
    return min(numbers), max(numbers)


# --- *args: variable positional arguments ---
def total(*args):
    """Return the sum of all provided numbers."""
    return sum(args)


# --- **kwargs: variable keyword arguments ---
def describe_person(**kwargs):
    """Print key-value pairs describing a person."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# --- Lambda (anonymous) function ---
square = lambda x: x * x  # noqa: E731


# --- Running examples ---
if __name__ == "__main__":
    print(greet("Bob"))
    print(power(3))          # 9  (uses default exponent=2)
    print(power(2, 10))      # 1024

    data = [4, 1, 7, 3, 9, 2]
    low, high = min_max(data)
    print(f"min={low}, max={high}")

    print(total(1, 2, 3, 4, 5))  # 15

    print("Person details:")
    describe_person(name="Carol", age=30, city="New York")

    print(square(7))  # 49
