# Write a Python program to count the values associated with key in a dictionary.
# student = [{'id': 1, 'success': True, 'name': 'Lary'},
#  {'id': 2, 'success': False, 'name': 'Rabi'},
#  {'id': 3, 'success': True, 'name': 'Alex'}]
# print(sum(d['success'] for d in student))

class Count_associated:
    def __init__(self, key):
        self.key = key
        self.student = [{'id': 1, 'success': True, 'name': 'Lary'},
                        {'id': 2, 'success': False, 'name': 'Rabi'},
                        {'id': 3, 'success': True, 'name': 'Alex'}]

    def coun(self):
        print(sum(d[self.key] for d in self.student))


C1 = Count_associated('success')
C1.coun()
