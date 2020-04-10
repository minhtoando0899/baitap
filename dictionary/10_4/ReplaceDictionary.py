# Write a Python program to replace dictionary values with their average.
# def sum_math_v_vi_average(list_of_dicts):
#     for d in list_of_dicts:
#         n1 = d.pop('V')
#         n2 = d.pop('VI')
#         d['V+VI'] = (n1 + n2)/2
#     return list_of_dicts
# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]
# print(sum_math_v_vi_average(student_details))
class ReplaceDictionary:
    def __init__(self, dict):
        self.dict = dict

    def rep(self):
        for x in self.dict:
            n1 = x.pop('V')
            n2 = x.pop('VI')
            x['V+VI'] = (n1 + n2) / 2
        return self.dict


R1 = ReplaceDictionary([
    {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
    {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
    {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
])
R1.rep()
print(R1.dict)
