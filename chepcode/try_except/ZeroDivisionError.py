while True:
    try:
        y = int(input("Enter your number: "))
        x = 10 / y
    except ZeroDivisionError as e:
        print("Error: %s" % e)
    except ValueError as r:
        print("Error: %s" % r)
    else:
        print(x)
    finally:
        print("End the program")
