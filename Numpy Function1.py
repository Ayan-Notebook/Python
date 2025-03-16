import numpy as np

# Input data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identify hot days (temperature exceeded 35 degrees Celsius)
hot_days = temperatures > 35

# Identify cold days (temperature dropped below 5 degrees Celsius)
cold_days = temperatures < 5

# Combine hot and cold days using logical OR
extreme_days = hot_days | cold_days

# Print the result
print("Days with extreme temperature conditions:")
print(temperatures[extreme_days])
