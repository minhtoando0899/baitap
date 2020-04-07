# Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def Check(key):
    if key in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictionary')


Check(5)
Check(9)