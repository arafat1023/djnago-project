"""
Module 4: Lists

This script demonstrates operations on lists.
"""

def list_operations():
    """Perform basic operations on a list."""
    my_list = [1, 2, 3]
    print("Original List:", my_list)

    # Append an element
    my_list.append(4)
    print("After Append:", my_list)

    # Remove an element
    my_list.remove(2)
    print("After Remove:", my_list)

    # Slice the list
    print("Sliced List (1:3):", my_list[1:3])

if __name__ == "__main__":
    list_operations()
