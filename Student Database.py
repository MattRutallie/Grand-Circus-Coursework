# Student Database
# 3 lists of student information
names = ["Shaquille O'Neal", "Anakin Skywalker", "Emma Watson"]
hometowns = ["Newark, New Jersey", "Tatooine", "Paris"]
favorite_foods = ["Fried Chicken", "Jogan Fruit", "Tacos"]

# program that makes use of the lists
while True:
    # Displays a list of all the students in a neat format
    print("\n==All Students==")
    for i in range(len(names)):
        print(f"{i + 1}. {names[i]}")

    student_num = input("\nEnter the number of the student you want to learn about: ")

    # This checks to see if the input can be converted to an integer
    if student_num.isdigit():
        student_num = int(student_num)
        # this now checks to see if said integer is valid
        if 1 <= student_num <= len(names):
            # Displays name of student requested
            print("\nStudent Information:")
            print("Name:", names[student_num - 1])
            # Asks user which category is to be viewed
            category = input("Enter 'Hometown' or 'Favorite Food': ").lower()
            while category not in ['hometown', 'favorite food']:
                print("Invalid category. Please enter 'Hometown' or 'Favorite Food'.")
                category = input("Enter 'Hometown' or 'Favorite Food': ").lower()

            # based on input, displayed what was requested
            if category == 'hometown':
                print("Hometown:", hometowns[student_num - 1])
            elif category == 'favorite food':
                print("Favorite Food:", favorite_foods[student_num - 1])
        else:
            print("Invalid student number. Please enter a number from 1 to", len(names))
    else:
        print("Invalid input. Please enter a number.")

    # this uses a nested loop to ask if the user wants to learn about another student
    while True:
        choice = input("\nDo you want to learn about another student? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    if choice == 'no':
        print("Thank you for using the student information program!")
        break

# end of program!
