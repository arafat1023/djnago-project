"""
Module 4: Dictionaries

This script demonstrates dictionary operations.
"""

def dictionary_operations():
    """Perform basic operations on a dictionary."""
    my_dict = {"a": 1, "b": 2}
    print("Original Dictionary:", my_dict)

    # Add an entry
    my_dict["c"] = 3
    print("Updated Dictionary:", my_dict)

    # Access a value
    print("Value for Key 'a':", my_dict["a"])

if __name__ == "__main__":
    dictionary_operations()
