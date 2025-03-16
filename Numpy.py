import numpy as np

# Task 1
my_list = [1, 2, 3, 4, 5]
numpy_array = np.array(my_list)
print("Task 1 Output:")
print(numpy_array)

# Task 2
my_list_task2 = [1, 2, 3, 4, 5]
numpy_array_task2 = np.array(my_list_task2)
print("\nTask 2 Output:")
print("Original Array:", numpy_array_task2)

# Displaying the first and last index
first_index = numpy_array_task2[0]
last_index = numpy_array_task2[-1]
print("First Index:", first_index)
print("Last Index:", last_index)

# Multiplying each element by 2
result_array = numpy_array_task2 * 2
print("Result after multiplying each element by 2:")
print(result_array)
