# tính tổng  S = 1*3*5 + 3*5*7 + ... + n*(n+2)*(n+4)
def Sum(n):
    a = []
    for i in range(1, n + 1, 2):
        S = i * (i + 2) * (i + 4)
        a.append(S)
    print(sum(a))


print(Sum(7))
