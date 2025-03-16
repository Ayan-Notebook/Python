def remove_duplicates(input_string):
    unique_chars = []

    for char in input_string:
        if char not in unique_chars:
            unique_chars.append(char)

    result_string = ''.join(unique_chars)
    print(f"Output: {result_string}")

# Example usage:
input_str = "String and String Function"
remove_duplicates(input_str)
