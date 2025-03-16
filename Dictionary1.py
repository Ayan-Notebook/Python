def calculate_mean(dictionary):
    if not dictionary:
        return None

    total = sum(dictionary.values())
    mean = total / len(dictionary)
    return mean

# Example usage:
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
mean_result = calculate_mean(test_dict)
print("Mean:", mean_result)
