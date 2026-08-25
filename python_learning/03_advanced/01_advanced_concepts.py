"""
Module 8: Advanced Python Concepts
=====================================
Decorators, generators, context managers, and comprehensions.
Copilot tip: these patterns are perfect for Copilot — start the signature and it fills in the body.
"""

import time
from contextlib import contextmanager


# ---------- Decorators ----------
def timer(func):
    """Decorator that prints how long a function takes to run."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timer] {func.__name__}() took {elapsed:.6f}s")
        return result
    return wrapper


def retry(max_attempts=3):
    """Decorator factory: retry a function up to max_attempts times on exception."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:  # noqa: BLE001
                    last_exc = exc
                    print(f"  attempt {attempt} failed: {exc}")
            print(f"All {max_attempts} attempts failed.")
            raise last_exc
        return wrapper
    return decorator


@timer
def slow_sum(n):
    """Return sum of 0..n."""
    return sum(range(n + 1))


# ---------- Generators ----------
def fibonacci(limit):
    """Yield Fibonacci numbers up to limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


def infinite_counter(start=0):
    """Infinite generator — yields incrementing integers."""
    n = start
    while True:
        yield n
        n += 1


# ---------- Context managers ----------
@contextmanager
def managed_resource(name):
    """Simple context manager that logs acquire/release."""
    print(f"Acquiring resource: {name}")
    try:
        yield name.upper()
    finally:
        print(f"Releasing resource: {name}")


# ---------- Advanced comprehensions ----------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten the matrix
flat = [cell for row in matrix for cell in row]

# Dictionary comprehension with condition
even_squares = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}

# Set comprehension
unique_lengths = {len(word) for word in ["python", "is", "fun", "and", "powerful"]}

# Generator expression (lazy)
gen_sum = sum(x ** 2 for x in range(1, 101))


# ---------- Running examples ----------
if __name__ == "__main__":
    print(slow_sum(1_000_000))

    print("\nFibonacci up to 100:", list(fibonacci(100)))

    counter = infinite_counter(10)
    print("Counter:", [next(counter) for _ in range(5)])

    with managed_resource("database connection") as res:
        print(f"Using: {res}")

    print("\nFlattened matrix:", flat)
    print("Even squares:", even_squares)
    print("Unique word lengths:", unique_lengths)
    print("Sum of squares 1–100:", gen_sum)
