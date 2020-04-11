def max(a, b=1000, c=2000):
    if a > b and a > c:
        print(a)
    else:
        if b > c:
            print(b)
        else:
            print(c)


max(3000)
max(3000, 5000)
max(3000, 4000, 5000)
