try:
    user_input = input("Enter an integer: ")
    integer_value = int(user_input)
    print("You entered:", integer_value)

except ValueError:
    print("Error: Please enter a valid integer.")
