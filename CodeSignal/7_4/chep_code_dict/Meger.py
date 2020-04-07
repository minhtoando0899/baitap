# Write a Python script to merge two Python dictionaries
dic1 = {1: 10, 2: 20, 3: 30}
dic2 = {4: 40, 5: 50, 6: 60}
dic1.update(dic2)
print(dic1)

d = dic1.copy()
d.update(dic2)
print(d)
