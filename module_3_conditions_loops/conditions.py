"""
Module 3: Conditional Statements

This script demonstrates the use of conditional statements in Python.
"""

def check_number():
    """Checks if a number is positive, negative, or zero."""
    num = int(input("Enter a number: "))
    if num > 0:
        print("The number is positive.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")

def is_even_or_odd():
    """Checks if a number is even or odd."""
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

if __name__ == "__main__":
    check_number()
    is_even_or_odd()
