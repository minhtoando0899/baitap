# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def Generate(key):
    d = dict()

    for x in range(1, key + 1):
        d[x] = x * x
    print(d)


Generate(10)
Generate(100)