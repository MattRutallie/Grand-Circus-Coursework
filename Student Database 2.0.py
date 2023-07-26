students = [
    {"name": "Shaquille O'Neal", "hometown": "Newark, New Jersey", "favorite_food": "Fried Chicken"},
    {"name": "Anakin Skywalker", "hometown": "Tatooine", "favorite_food": "Jogan Fruit"},
    {"name": "Emma Watson", "hometown": "Paris", "favorite_food": "Tacos"}
]


# Function to display all students
def list_students():
    print("\n== All Students ==")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']}")


# Function to get a valid student index from the user
def get_student_index():
    while True:
        student_num = input("\nEnter the number of the student you want to learn about: ")
        if student_num.isdigit() and 1 <= int(student_num) <= len(students):
            return int(student_num)
        else:
            print("Invalid student number. Please enter a number from 1 to", len(students))


# Function to display student information
def display_student_info(student_index):
    student = students[student_index - 1]
    print("\nStudent Information:")
    print("Name:", student['name'])
    category = input("Enter 'Hometown' or 'Favorite Food': ").lower()
    while category not in ['hometown', 'favorite food']:
        print("Invalid category. Please enter 'Hometown' or 'Favorite Food'.")
        category = input("Enter 'Hometown' or 'Favorite Food': ").lower()

    if category == 'hometown':
        print("Hometown:", student['hometown'])
    elif category == 'favorite food':
        print("Favorite Food:", student['favorite_food'])


# Main program
while True:
    list_students()
    student_index = get_student_index()
    display_student_info(student_index)

    while True:
        choice = input("\nDo you want to learn about another student? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    if choice == 'no':
        print("Thank you for using the student information program!")
        break

# End of program!