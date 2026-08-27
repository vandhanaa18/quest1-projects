"""Main integration module for student management system."""

import sys
from student_data import Student, StudentManager
from grade_calculator import GradeCalculator
from display_info import (
    display_all_students,
    display_student_details,
    display_course_performance_report,
    display_summary
)


def print_separator():
    """Print a separator line for better visual formatting."""
    print("\n" + "=" * 70)


def main_menu():
    """Display the main menu and return user choice."""
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add a new student")
    print("2. Display all students")
    print("3. Display specific student details")
    print("4. Calculate grades for a student")
    print("5. Display course performance report")
    print("6. Exit")
    
    try:
        choice = input("\nEnter your choice (1-6): ").strip()
        return choice
    except EOFError:
        return 'q'


def get_student_id(prompt="Enter student ID: "):
    """Get a valid student ID from user."""
    while True:
        student_id = input(prompt).strip()
        if student_id:
            return student_id
        print("Student ID cannot be empty.")


def add_student(interaction_mode=False, manager=None):
    """Add a new student to the system.
    
    Args:
        interaction_mode: If True, get input from user. If False, use defaults for demo.
        manager: StudentManager instance.
        
    Returns:
        The created student object or None if not added.
    """
    if interaction_mode:
        print("\n--- ADD NEW STUDENT ---")
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return None
        
        manager.add_student(name, get_student_id())
        
        # Add courses
        while True:
            course_name = input(f"Add another course for {name} (or 'done' to finish): ").strip()
            if course_name.lower() == 'done':
                break
            manager.add_course_for_student(manager._students.get(name).student_id, course_name)
        
        return manager.get_student(get_student_id())
    
    else:
        # Demo mode - auto-populate with sample data
        print("\n--- ADDING DEMO STUDENT ---")
        manager.add_student("John Smith", "S001", ["Math 101", "Science 201"])
        manager.add_course_for_student("S001", "English 301")
        return None


def set_grades(student_id, calculator):
    """Set grades for a student's courses.
    
    Args:
        student_id: ID of the student to grade.
        calculator: GradeCalculator instance.
        
    Returns:
        Formatted string with updated student info.
    """
    student = manager.get_student(student_id)
    if not student:
        return f"Student '{student_id}' not found."
    
    lines = []
    for course in student.courses:
        while True:
            try:
                grade_input = input(f"Enter grade (0-100) or letter (A-F) for {course}: ").strip()
                
                # Validate and convert grade
                if len(grade_input) == 1 and grade_input.upper() in ['A', 'B', 'C', 'D', 'F']:
                    numeric_grade = calculator.convert_letter_to_numeric(grade_input)
                else:
                    numeric_grade = float(grade_input)
                
                if 0 <= numeric_grade <= 100:
                    student.set_grade(course, numeric_grade)
                    break
                else:
                    print("Please enter a valid grade (0-100 or A-F).")
            except ValueError:
                print("Invalid input. Please enter a number between 0-100 or a letter grade.")
    
    return student


def display_courses_for_student(student):
    """Display available courses for grading."""
    if not hasattr(student, 'courses'):
        return []
    return [f"Course: {course}" for course in sorted(student.courses)]


def calculate_and_display_grades(student_id):
    """Calculate grades and display result for a student.
    
    Args:
        student_id: ID of the student to process.
        
    Returns:
        Formatted string with grade calculation results.
    """
    student = manager.get_student(student_id)
    if not student:
        return f"Student '{student_id}' not found."
    
    lines = []
    for course in student.courses:
        current_grade = student.get_grade(course)
        letter_grade = calculator.calculate_letter_grade(current_grade) if isinstance(current_grade, (int, float)) else "N/A"
        
        lines.append(f"{course}: {current_grade} ({letter_grade})")
    
    avg_grade = calculator.calculate_average_grade(student.grades)
    gpa = calculator.calculate_gpa(student.grades)
    
    lines.extend([
        f"\nAverage Grade: {avg_grade:.2f}",
        f"GPA:           {gpa:.2f}" if gpa else "GPA:          N/A"
    ])
    
    return "\n".join(lines)


def main():
    """Main function to run the student management system."""
    print_separator()
    print("WELCOME TO STUDENT MANAGEMENT SYSTEM")
    print_separator()
    
    # Initialize components
    global manager, calculator
    manager = StudentManager()
    calculator = GradeCalculator()
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            add_student(interaction_mode=True, manager=manager)
        elif choice == '2':
            students = manager.get_all_students()
            print(display_all_students(students))
        elif choice == '3':
            student_id = input("Enter student ID to view details: ").strip()
            if student_id:
                student = manager.get_student(student_id)
                if student:
                    print(display_student_details(student))
                else:
                    print(f"Student '{student_id}' not found.")
        elif choice == '4':
            student_id = input("Enter student ID to calculate grades: ").strip()
            if student_id:
                result = calculate_and_display_grades(student_id)
                print(result)
        elif choice == '5':
            student_id = input("Enter student ID for course report: ").strip()
            if student_id:
                student = manager.get_student(student_id)
                if student:
                    grades = dict(student.grades)
                    report = calculator.get_course_performance_report(grades)
                    print(report)
        elif choice == '6':
            print("\nThank you for using the Student Management System!")
            print_separator()
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSystem terminated by user.")
    except Exception as e:
        print(f"\nError occurred: {e}")