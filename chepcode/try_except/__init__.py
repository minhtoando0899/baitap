try:
    print(range(len(-8)))
except:
    print("object of type 'int' has no len()")
else:
    print("true")
finally:
    print("The 'try_except' is finished")
