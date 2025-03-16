import numpy as np

# Input data
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Reshape the array into a 2D array with 4 columns (quarters)
quarterly_reports = monthly_sales.reshape(-1, 3)

# Print the result
print("Quarterly reports:")
print(quarterly_reports)
