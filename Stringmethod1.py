def count_characters(input_string):
    chars = 0
    digits = 0
    symbols = 0

    for char in input_string:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    print(f"Chars = {chars} Digits = {digits} Symbols = {symbols}")

# Example usage:
input_str = "P@#yn26at^&i5ve"
count_characters(input_str)
