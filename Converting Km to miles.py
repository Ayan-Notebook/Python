# Program to convert kilometers to miles using if-else

# Taking input from the user
kilometers = float(input("Enter distance in kilometers: "))

# Conversion factor
conversion_factor = 0.621371

# Checking if the input is non-negative
if kilometers >= 0:
    # Calculating miles
    miles = kilometers * conversion_factor
    print(f"{kilometers} kilometers is equal to {miles} miles.")
else:
    print("Please enter a non-negative distance.")
