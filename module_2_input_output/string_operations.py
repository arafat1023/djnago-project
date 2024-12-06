"""
Module 2: String Operations

This script demonstrates basic string operations in Python.
"""


def string_operations():
    """Performs various string operations."""
    text = input("Enter a string: ")
    print("\n=== String Operations ===")
    print(f"Original String: {text}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Title Case: {text.title()}")
    print(f"Reversed: {text[::-1]}")
    print(f"Length: {len(text)}")


if __name__ == "__main__":
    string_operations()
