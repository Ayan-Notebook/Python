basic_pay = float(input("Enter the employee's basic pay: "))

if basic_pay < 5000:
    da_rate = 0.10
    hra_rate = 0.23
elif 5000 <= basic_pay < 50000:
    da_rate = 0.15
    hra_rate = 0.25
elif 50000 <= basic_pay < 100000:
    da_rate = 0.20
    hra_rate = 0.28
else:
    da_rate = 0.25
    hra_rate = 0.30

da = basic_pay * da_rate
hra = basic_pay * hra_rate
gross_Salary = basic_pay + da + hra

print("\nBasic Pay:", basic_pay)
print("DA:", da)
print("HRA:", hra)
print("Gross Salary:", gross_Salary)
