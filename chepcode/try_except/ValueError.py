while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError as v:
        print("That was no valid number. Try again...")
        print("Error :%s" % v)
