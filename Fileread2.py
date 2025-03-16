def count_and_display_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            total_words = len(words)
            print(f"Total number of words in '{filename}': {total_words}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage:
filename = "ABC.txt"
count_and_display_words(filename)
