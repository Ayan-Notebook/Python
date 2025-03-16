
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 <= num2:
    if num1 <= num3:
        minimum = num1
    else:
        minimum = num3
else:
    if num2 <= num3:
        minimum = num2
    else:
        minimum = num3

print("The minimum integer value is:", minimum)
