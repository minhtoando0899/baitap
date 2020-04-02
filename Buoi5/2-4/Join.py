# Write a Python program to convert a list of characters into a string.
class Str:
    def __init__(self, list):
        self.list = list
        self.str_1 = str

    def join(self):
        self.str_1 = ''.join(self.list)


J1 = Str(["a", "n", "h ", "y", "e", "u ", "e", "m"])
J1.join()
print(J1.str_1)
