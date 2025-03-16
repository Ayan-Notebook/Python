import matplotlib.pyplot as plt

# Input data
days = list(range(1, 78))
stock_prices = [100, 105, 110, 115, 112, 120, 118, 125, 128, 130, 132, 135, 138, 140, 142, 144, 145, 148,
                150, 155, 160, 158, 162, 165, 170, 172, 175, 178, 180, 182, 185, 188, 190, 192, 195, 198,
                200, 198, 195, 193, 190, 188, 185, 182, 180, 178, 175, 172, 170, 168, 165, 162, 160, 158,
                155, 152, 150, 148, 145, 143, 140, 138, 135, 132, 130, 128, 125, 123, 120, 118, 115, 112,
                110, 108, 105, 103, 100]

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(days, stock_prices, marker='o', linestyle='-', color='b')
plt.title('Daily Closing Prices of the Stock Over a Year')
plt.xlabel('Days')
plt.ylabel('Closing Price')
plt.grid(True)
plt.show()
