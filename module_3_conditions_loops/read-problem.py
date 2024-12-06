"""
Module 3: Real-World Problem

This script demonstrates the application of conditions and loops
to solve a real-world problem.
"""

def calculate_grades():
    """
    Calculates the average grade for students and determines the highest grade.
    """
    print("Enter student grades (enter -1 to stop):")
    grades = []
    while True:
        grade = int(input("Grade: "))
        if grade == -1:
            break
        grades.append(grade)

    if not grades:
        print("No grades entered.")
        return

    avg_grade = sum(grades) / len(grades)
    highest_grade = max(grades)

    print("\n=== Results ===")
    print(f"Average Grade: {avg_grade:.2f}")
    print(f"Highest Grade: {highest_grade}")

if __name__ == "__main__":
    calculate_grades()
