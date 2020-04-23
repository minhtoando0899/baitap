import math

a = [12, 32, 16]
for x in a:
    if math.sqrt(x) == int(math.sqrt(x)):
        print(x)
print(len(a))