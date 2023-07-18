user_input = int(input("Enter an integer between 1 and 100 (inclusive): "))

if user_input % 2 == 1 and user_input < 60:
    print(f"{user_input} is Odd and less than 60.")
elif user_input % 2 == 0 and 2 <= user_input <= 24:
    print("Even and less than 25.")
elif user_input % 2 == 0 and 26 <= user_input <= 60:
    print("Even and between 26 and 60 (inclusive).")
elif user_input % 2 == 0 and user_input > 60:
    print(f"{user_input} is Even and greater than 60.")
elif user_input % 2 == 1 and user_input > 60:
    print(f"{user_input} is Odd and greater than 60.")
else:
    print("Invalid input. The integer should be between 1 and 100 (inclusive).")
