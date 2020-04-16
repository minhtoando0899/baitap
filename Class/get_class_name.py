# Write a Python program to get the class name of an instance in Python.

import itertools

x = itertools.cycle('TOAN')
print(type(x).__name__)
