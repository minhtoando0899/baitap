while True:
    try:
        d = {"1": "a",
             "2": "b"}

        key = input("Enter the key: ")

        x = d[key]
        print(x)
    except KeyError:
        print("Error: ")
    finally:
        print("_____________")
