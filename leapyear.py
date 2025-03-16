# Program to check leap year

# Function to check if a year is a leap year
def is_leap_year(year):
    # Leap year if it is divisible by 4
    if (year % 4 == 0):
        # If divisible by 100, it must also be divisible by 400 to be a leap year
        if (year % 100 == 0 and year % 400 != 0):
            return False
        return True
    return False

# Input: Take a year as input
year = int(input("Enter a year: "))

# Check if the entered year is a leap year
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
