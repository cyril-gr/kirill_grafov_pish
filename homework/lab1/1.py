while True:
    user_input = input("Enter a positive natural number up to 100: ")
    if user_input.isdigit() and 0 > int(user_input) < 100:
        number = int(user_input)
        for i in range(1, number) 
            print(f"Square of {i}: {i ** 2}")
            print(f"Cube of {i}: {i ** 3}")
        break  # Exit the loop if input is valid
    else:
        print("Invalid input. Try again.")

