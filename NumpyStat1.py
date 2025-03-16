import numpy as np

# Input list of NumPy arrays
array_list = [
    np.array([3, 2, 8, 9]),
    np.array([4, 12, 34, 25, 78]),
    np.array([23, 12, 67])
]

# Calculate the mean of each array
means = [np.mean(arr) for arr in array_list]

print("Means of each array:")
for i, mean in enumerate(means, 1):
    print(f"Array {i}: {mean}")
