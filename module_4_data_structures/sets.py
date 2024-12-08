"""
Module 4: Sets

This script demonstrates set operations.
"""

def set_operations():
    """Perform basic operations on sets."""
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    print("Set A:", set_a)
    print("Set B:", set_b)

    # Union
    print("Union:", set_a | set_b)

    # Intersection
    print("Intersection:", set_a & set_b)

    # Difference
    print("Difference:", set_a - set_b)

if __name__ == "__main__":
    set_operations()
