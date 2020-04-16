# Write a Python program to reverse a string word by word.
class Reverse:
    def rev(self, s):
        return '...'.join(reversed(s.split()))


print(Reverse().rev('Minh Toan Do'))
