
import pickle
import os

FILE_NAME = "students.dat"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "rb") as file:
            return pickle.load(file)
    return {}

def save_students(students):
    with open(FILE_NAME, "wb") as file:
        pickle.dump(students, file)

def add_student():
    students = load_students()
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    students[roll] = {
        "Name": name,
        "Course": course,
        "Marks": marks
    }

    save_students(students)
    print("Student added successfully!")

def view_students():
    students = load_students()
    if not students:
        print("No records found.")
        return

    for roll, data in students.items():
        print("\nRoll Number:", roll)
        print("Name :", data["Name"])
        print("Course :", data["Course"])
        print("Marks :", data["Marks"])

def search_student():
    students = load_students()
    roll = input("Enter Roll Number to search: ")

    if roll in students:
        data = students[roll]
        print("Name :", data["Name"])
        print("Course :", data["Course"])
        print("Marks :", data["Marks"])
    else:
        print("Student not found!")

def update_student():
    students = load_students()
    roll = input("Enter Roll Number to update: ")

    if roll not in students:
        print("Student not found!")
        return

    name = input("Enter new Name: ")
    course = input("Enter new Course: ")
    marks = input("Enter new Marks: ")

    students[roll] = {
        "Name": name,
        "Course": course,
        "Marks": marks
    }

    save_students(students)
    print("Record updated successfully!")

def delete_student():
    students = load_students()
    roll = input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        save_students(students)
        print("Record deleted successfully!")
    else:
        print("Student not found!")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
