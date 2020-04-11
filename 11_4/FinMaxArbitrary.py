def Max(*num):
    max = num[0]
    for x in num:
        if max < x:
            max = x
    print(max)


Max(1, 2, 3, 4, 5, 6, 7331, 8, 9, 10)
