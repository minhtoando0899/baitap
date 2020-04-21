# 9. Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.
class String:
    def __init__(self):
        self.str_1 = ""

    def get(self):
        self.str_1 = input("Enter your str: ")

    def pri(self):
        print(self.str_1.upper())


str_1 = String()
str_1.get()
str_1.pri()
