"""
Solutions to exercises.py
===========================
Compare these with your own solutions — there is often more than one correct approach!
"""

import os
from collections import Counter


# -----------------------------------------------------------------------
# Exercise 1 — FizzBuzz
# -----------------------------------------------------------------------
def fizzbuzz(n):
    """Return a list of FizzBuzz strings for numbers 1 through n."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# -----------------------------------------------------------------------
# Exercise 2 — Palindrome checker
# -----------------------------------------------------------------------
def is_palindrome(text):
    """Return True if text is a palindrome (ignoring case and spaces)."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# -----------------------------------------------------------------------
# Exercise 3 — Word frequency counter
# -----------------------------------------------------------------------
def word_frequency(sentence):
    """Return a dict of word -> count for each word in sentence."""
    words = sentence.lower().split()
    return dict(Counter(words))


# -----------------------------------------------------------------------
# Exercise 4 — Simple Stack class
# -----------------------------------------------------------------------
class Stack:
    """LIFO stack implemented with a Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push an item onto the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item; raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it; raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek at an empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack has no items."""
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items!r})"


# -----------------------------------------------------------------------
# Exercise 5 — Temperature converter
# -----------------------------------------------------------------------
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15


# -----------------------------------------------------------------------
# Exercise 6 — File word count
# -----------------------------------------------------------------------
def count_words(filepath):
    """Return the total number of whitespace-separated words in a text file."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath) as fh:
        return sum(len(line.split()) for line in fh)


# -----------------------------------------------------------------------
# Self-test
# -----------------------------------------------------------------------
if __name__ == "__main__":
    # FizzBuzz
    fb = fizzbuzz(15)
    assert fb[2] == "Fizz"
    assert fb[4] == "Buzz"
    assert fb[14] == "FizzBuzz"
    print("FizzBuzz (1-15):", fb)

    # Palindrome
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False
    print("\nPalindrome checks passed.")

    # Word frequency
    freq = word_frequency("to be or not to be")
    assert freq["to"] == 2
    assert freq["be"] == 2
    print("\nWord frequencies:", freq)

    # Stack
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3
    assert s.pop() == 3
    assert len(s) == 2
    print("\nStack operations passed.")

    # Temperature
    assert celsius_to_fahrenheit(0) == 32
    assert fahrenheit_to_celsius(212) == 100
    assert celsius_to_kelvin(0) == 273.15
    print("\nTemperature conversions passed.")

    print("\nAll solution tests passed!")
