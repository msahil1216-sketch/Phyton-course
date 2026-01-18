try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Error: Age must be positive!")
    else:
        if age % 2 == 0:
            print(f"Age {age} is even.")
        else:
            print(f"Age {age} is odd.")

except ValueError:
    print("Error: Please enter a valid integer (no decimals, letters, or symbols)!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")