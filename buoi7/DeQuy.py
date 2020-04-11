def change2(i):
    if i == 1:
        return 1
    s = ''
    while i >= 1:
        if i % 2 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return s


print(change2(71))
