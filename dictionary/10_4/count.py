# Write a Python program to count number of items in a dictionary value that is a list
class Count:
    def __init__(self, dict):
        self.dict = dict


    def cou(self):
        ctr = sum(map(len, self.dict.values()))
        print(ctr)


C1 = Count({'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']})
C1.cou()
