import matplotlib.pyplot as plt

# Customer names and their corresponding sales
customer_names = ["Customer1", "Customer2", "Customer3", "Customer4", "Customer5"]
sales = [15000, 22000, 18000, 25000, 20000]

# Plotting the bar graph
plt.bar(customer_names, sales, color='blue')
plt.title('Sales Comparison by Customer')
plt.xlabel('Customer Names')
plt.ylabel('Sales (in dollars)')
plt.show()
