def is_palindrome(num):
    original_num = num
    reverse_num = 0
    
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num = num // 10

    return original_num == reverse_num

number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
