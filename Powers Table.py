continue_program = True

while continue_program:
    num = int(input("Enter an integer: "))
    print("Number | Square | Cube")
    print("-----------------------")
    for i in range(1, num + 1):
        square = i ** 2
        cube = i ** 3
        print(f"{i:6} | {square:6} | {cube:4}")

    while True:
        choice = input("Would you like to continue? (yes/no): ")
        if choice.lower() == 'yes':
            break
        elif choice.lower() == 'no':
            print("Thank you for using the program!")
            continue_program = False
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    if not continue_program:
        break