try:
    age_input = input("Enter your age: ")
    age = int(age_input)  # Try converting the input to an integer

    if age <= 0 or age > 130:
        print("Error: Please enter a valid age between 1 and 130.")
    else:
        if age % 2 == 0:
            print(f"The age {age} is even.")
        else:
            print(f"The age {age} is odd.")

except ValueError:
    print("Invalid input! Please enter a number.")
