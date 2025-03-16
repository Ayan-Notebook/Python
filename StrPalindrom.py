def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = s.lower()
    
    # Compare the original string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage:
user_input = input("Enter a string: ")
result = is_palindrome(user_input)

if result:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
