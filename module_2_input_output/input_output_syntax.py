"""
Module 2: Python Basics – Input, Output, and Syntax

This script demonstrates Python's input/output mechanisms, variables,
and string operations.
"""


def get_user_details():
    """Collects user details and returns a formatted string."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    location = input("Enter your location: ")
    return f"Name: {name}, Age: {age}, Location: {location}"


def display_message(details):
    """Displays a structured message based on user details."""
    print("\n=== User Details ===")
    print(details)


if __name__ == "__main__":
    user_details = get_user_details()
    display_message(user_details)
