# Program for Toy Vendor Discount

# Function to calculate the net amount after discount
def calculate_discount(product_code, order_amount):
    discount_percentage = 0

    # Check product code and set discount percentage accordingly
    if product_code == 1 and order_amount > 1000:
        discount_percentage = 10
    elif product_code == 2 and order_amount > 100:
        discount_percentage = 5
    elif product_code == 3 and order_amount > 500:
        discount_percentage = 10

    # Calculate the net amount after discount
    discount_amount = (discount_percentage / 100) * order_amount
    net_amount = order_amount - discount_amount

    return net_amount

# Input: Take product code and order amount as input
product_code = int(input("Enter product code (1 for Battery, 2 for Key, 3 for Electrical): "))
order_amount = float(input("Enter order amount: "))

# Calculate and print the net amount after discount
net_amount = calculate_discount(product_code, order_amount)
print(f"Net amount after discount: Rs. {net_amount:.2f}")
