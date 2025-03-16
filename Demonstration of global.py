# This code shows the use of local and global variables with the same name

variable_name = "Global"

def example_function():
    variable_name = "Local"
    print("Inside function - Local Variable:", variable_name)

# Accessing the global variable
print("Global Variable before function call:", variable_name)

# Calling the function
example_function()

# Accessing the global variable after the function call
print("Global Variable after function call:", variable_name)
