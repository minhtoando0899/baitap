# # Write a Python program to split a list based on first character of word.
# from itertools import groupby
# from operator import itemgetter
#
# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
#
# for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
#     print(letter)
#     for word in words:
#         print(word)
from itertools import groupby
from operator import itemgetter


class Slip_List_first_character:
    def __init__(self, list):
        self.list = list

    def sli(self):
        for letter, words in groupby(sorted(self.list), key=itemgetter(0)):
            print(letter)
            for word in words:
                print(word)


S1 = Slip_List_first_character(['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
                                'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave',
                                'call'])
S1.sli()
print(S1.sli())
