def read_and_display(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # Displaying each line without leading/trailing whitespace
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage:
filename = "ABC.txt"
read_and_display(filename)
