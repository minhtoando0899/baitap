import math
a = 430.833
b = 470
c = 472.4
d = 467.6
e = 471.75
f = 468.25
g = 235
t = float(math.sqrt(((b - a) ** 2 + (c - a) ** 2 + (d - a) ** 2 + (e - a) ** 2 + (f - a) ** 2 + (g - a) ** 2)/5))
print(t*3.36)
print((t/(math.sqrt(6)))*3.36)
