"""
Module 6: Error Handling
=========================
Learn try/except/finally and how to create custom exceptions.
Copilot tip: write `# handle the case where ...` and let Copilot suggest the except block.
"""


# ---------- Custom exception ----------
class InvalidAgeError(ValueError):
    """Raised when an age value is outside the accepted range."""


# ---------- Basic try/except/finally ----------
def safe_divide(a, b):
    """Divide a by b, returning None on division by zero."""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
        return None
    else:
        # runs only if no exception was raised
        return result
    finally:
        # always runs
        print("safe_divide() finished.")


# ---------- Multiple except clauses ----------
def parse_integer(value):
    """Convert value to int, handling common errors gracefully."""
    try:
        return int(value)
    except (ValueError, TypeError) as exc:
        print(f"Conversion failed: {exc}")
        return None


# ---------- Raising custom exceptions ----------
def set_age(age):
    """Store age if valid; raise InvalidAgeError otherwise."""
    if not isinstance(age, int) or age < 0 or age > 150:
        raise InvalidAgeError(f"Age must be an integer between 0 and 150, got: {age!r}")
    return age


# ---------- Running examples ----------
if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))

    print(parse_integer("42"))
    print(parse_integer("abc"))
    print(parse_integer(None))

    try:
        set_age(200)
    except InvalidAgeError as exc:
        print(f"Caught: {exc}")

    print(f"Valid age: {set_age(25)}")
