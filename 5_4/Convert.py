# # Write a Python program to convert a string to a list.
# import ast
# color ="['Red', 'Green', 'White']"
# print(ast.literal_eval(color))
import ast


class Convert:
    def __init__(self, str):
        self.list = str

    def con(self):
        print(ast.literal_eval(self.list))


C1 = Convert("['Red', 'Green', 'White']")
C1.con()
