# Write a Python program to sort a list of dictionaries using Lambda.
class Sort:
    def __init__(self, list):
        self.list = list

    def sor(self):
        a = sorted(self.list, key=lambda x: x['color'])
        print(a)


S1 = Sort([{'make': 'Nokia', 'model': 216, 'color': 'Black'},
           {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
           {'make': 'Samsung', 'model': 7, 'color': 'Blue'}])
S1.sor()
