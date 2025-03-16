def find_max_min(numbers):
    if not numbers:
        return None, None  # Return None for both min and max if the list is empty

    min_num = max_num = numbers[0]  # Initialize min and max with the first element

    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return min_num, max_num

# Example usage:
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = find_max_min(my_numbers)
print("Smallest number:", min_value)
print("Largest number:", max_value)
