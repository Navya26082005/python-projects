students = []

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        student = {
            "Name": name,
            "Roll": roll,
            "Marks": marks
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        print("\nStudent List:")
        for s in students:
            print(s)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")