from scipy import integrate
def my_function(x):
    return x**2

lower_limit = 0
upper_limit = 2

result, error = integrate.quad(my_function, lower_limit, upper_limit)

print("Result of integration:", result)
print("Estimated error:", error)
