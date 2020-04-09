#  Write a Python program to remove spaces from dictionary keys
class Remove_spaces:
    def __init__(self, dict):
        self.dict = dict

    def rem(self):
        new_dict = {x.translate({32: None}): y for x, y in self.dict.items()}
        print(new_dict)


R1 = Remove_spaces({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})
R1.rem()
