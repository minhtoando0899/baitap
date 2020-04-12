# Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number.
def mun(n):
    return lambda x: x * n


result = mun(5)
print(result(15))
result = mun(6)
print(result(15))
