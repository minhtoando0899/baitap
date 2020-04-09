# Write a Python program to sort a dictionary by key.
# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}
#
# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))
import operator


class Sort:
    def __init__(self, dict):
        self.dict = dict

    def sor(self):
        for key in sorted(self.dict):
            print("%s : %s" % (key, self.dict[key]))


S1 = Sort({'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'})
S1.sor()
