# Module 1: Overview of Python

## Objectives
- Understand Python's purpose and its application.
- Install Python and basic development tools.
- Create a simple Python script to demonstrate the environment setup.

## Tasks
- Install Python and verify the installation.
- Set up a virtual environment for the project.
- Write a script to greet the user.

## Steps
1. **Install Python**:
   - Download Python from [python.org](https://www.python.org/downloads/).
   - Verify the installation:
     ```bash
     python --version
     ```

2. **Set Up Virtual Environment**:
   - Create a virtual environment:
     ```bash
     python3 -m venv django-env
     ```
   - Activate the virtual environment:
     - **Linux/Mac**:
       ```bash
       source django-env/bin/activate
       ```
     - **Windows**:
       ```bash
       django-env\Scripts\activate
       ```

3. **Write the Script**:
   - Create a `introduction.py` file:
     ```python
     def greet_user(name: str) -> None:
         """Greets the user by name."""
         print(f"Hello, {name}! Welcome to Python learning.")

     if __name__ == "__main__":
         name = input("Enter your name: ")
         greet_user(name)
     ```

4. **Test the Script**:
   - Run the script:
     ```bash
     python3 introduction.py
     ```

## Best Practices
- Use type hints for functions.
- Add docstrings to explain the purpose of each function and script.
- Use `pylint` for linting and `black` for formatting.

## Additional Notes
- This module is the foundation for the project, ensuring a clear understanding of Python basics.
