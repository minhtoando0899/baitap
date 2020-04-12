def change2(n):
    if n == 0:
        return 0
    else:
        s = (change2(n // 2)) % 2
        return s


print(change2(6))
