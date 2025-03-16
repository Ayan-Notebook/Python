# Global variable
same_name_var = "I am a global variable"

def example_function():
    # Local variable with the same name
    same_name_var = "I am a local variable"
    print("Inside function:", same_name_var)

example_function()
# Accessing the global variable with the same name outside the function
print("Outside function:", same_name_var)
