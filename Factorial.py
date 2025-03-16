def factorial(n):
    result = 1
    
    while n > 1:
        result *= n
        n -= 1

    return result

number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}")
