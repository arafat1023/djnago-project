"""
Module 3: Loops

This script demonstrates the use of `for` and `while` loops in Python.
"""

def for_loop_example():
    """Prints numbers from 1 to 5 using a `for` loop."""
    print("For Loop Example:")
    for i in range(1, 6):
        print(f"Iteration {i}")

def while_loop_example():
    """Prints numbers from 1 to 5 using a `while` loop."""
    print("\nWhile Loop Example:")
    count = 1
    while count <= 5:
        print(f"Iteration {count}")
        count += 1

if __name__ == "__main__":
    for_loop_example()
    while_loop_example()
