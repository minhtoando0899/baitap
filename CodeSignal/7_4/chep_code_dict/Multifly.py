# Write a Python program to multiply all the items in a dictionary.
result = 1
dic1 = {1: 200, 2: 300, 3: 400}
for value in dic1:
    result = result * dic1[value]

print(result)
