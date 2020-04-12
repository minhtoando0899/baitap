# Write a Python program to check whether a given string is number or not using Lambda.


so = lambda x:x.replace('.','',1).isdigit()
print(so('1111'))
print(so('asda'))
