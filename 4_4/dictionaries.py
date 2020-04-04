# # Write a Python program to convert list to list of dictionaries.
# color_name = ["Black", "Red", "Maroon", "Yellow"]
# color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
# print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])

class Dictionaries:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def dic(self):
        print([{'color_name': f, 'color_code': c} for f, c in zip(self.list_1, self.list_2)])
D1 = Dictionaries(["Black", "Red", "Maroon", "Yellow"],["#000000", "#FF0000", "#800000", "#FFFF00"])
D1.dic()
