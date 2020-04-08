# Write a Python program to remove duplicates from Dictionary.
# student_data = {'id1':
#    {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id2':
#   {'name': ['David'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id3':
#     {'name': ['Sara'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
#  'id4':
#    {'name': ['Surya'],
#     'class': ['V'],
#     'subject_integration': ['english, math, science']
#    },
# }
#
# result = {}
#
# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value
#
# print(result)

class Remove:
    def __init__(self, dict):
        self.dict = dict
        self.result = {}

    def rem(self):
        for key, value in self.dict.items():
            if value not in self.result.values():
                self.result[key] = value
        print(self.result)


R1 = Remove({
    'id1':
        {'name': ['Sara'],
         'class': ['V'],
         'subject_integration': ['english, math, science']
         },
    'id2':
        {'name': ['David'],
         'class': ['V'],
         'subject_integration': ['english, math, science']
         },
    'id3':
        {'name': ['Sara'],
         'class': ['V'],
         'subject_integration': ['english, math, science']
         },
    'id4':
        {'name': ['Surya'],
         'class': ['V'],
         'subject_integration': ['english, math, science']
         },
})
R1.rem()
