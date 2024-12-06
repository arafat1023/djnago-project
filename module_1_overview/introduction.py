def greet_user(name: str) -> None:
    print(f"Hello, {name}! Welcome to Python learning.")


if __name__ == "__main__":
    name = input("Enter your name: ")
    greet_user(name)