# Syntax
if 5 > 2:
    print("correct")
# Variables
x = 5  # x is int
y = "Toan"  # y is str
print(x)
print(y)
# Data Type
x = 5
print(type(x))
x = "hello"
print(type(x))
x = 5.5
print(type(x))
x = 1j
print(type(x))
x = [1, 3, 4, 5]
print(type(x))
x = (1, 3, 5, 6)
print(type(x))
x = range(6)
print(type(x))
x = {1: 2, 3: "hello"}
print(type(x))
x = {1, 3, 4, "jone"}
print(type(x))
x = (1, 5.5, (1, 2, 3), [1, 2, 3], {3, 2, 1}, 1j, range(5), "true", bytearray(6), bytes(5), memoryview(bytes(3)))
for a in x:
    print(type(a))
# Number
import random

print(random.randrange(1, 1000000000000))
x = float(5)
y = int(3.2)
z = complex(5j)
print(x, y, z)
# String
a = " Em chao a Toan "
print(a[1])
a = " Em chao a Toan "
print(a[-5])
a = " Em chao a Toan "
print(a.strip())  # xoa dau cach 2 dau
a = " Em chao a Toan "
print(a.upper())  # chu in hoa
a = " Em chao a Toan "
print(a.lower())  # chu thuong
a = " Em chao a Toan "
print(a.replace("T", "H"))  # thay the chu trong cau
a = " Em chao a Toan "
x = "Toan" in a  # Kiem tra
print(x)
a = " Em chao a Toan "
x = "Em" in a
print(x)
a = "anh"
b = " ghet"
c = " em"
d = a + b + c
print(d)
c = "xin"
b = "ạ"
d = "phép"
a = " Em {0} {2} chao a Toan {1}"
print(a.format(c, b, d))  # them tu vao dau {}
# Booleans
print(9 == 10)
x = 115.5
print(isinstance(x, float))  # Kiem tra xem x co phai so thuc khong
# Operators
x = 5
y = 2
print(x + y, x - y, x * y, x / y, x % y, x ** y, x // y)
# List
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[9] = 0
print(a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 2 in a:
    print("yes")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(a))
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.append(11)
print(a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.insert(0, 0)
print(a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.remove(10)
print(a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.pop()
print(a)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del a[7]
print(a)
# Tuples
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = list(a)
b.append(11)  # Muon them data thi phai dung list
a = tuple(b)
print(a)
a = (1, 2, 3)
b = ("a", "b", "c")  # Hoac them 1 tuples khac de ghep vao
c = a + b
print(c)
# Set
a = {1, 2, 3, 4, 5}
a.add("toan")
print(a)
a = {1, 2, 3, 4, 5}
a.update([6, 7, 8, 9])
print(a)
a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9}
c = a.union(b)
print(c)
# dict
a = {
    "Ho": "Do",
    "Ten dem": "Minh",
    "Ten": "Toan"
}
print(a)
x = a.get("Ho")
print(x)
for x in a:
    print(x)
for x in a:
    print(a[x])
for x in a.values():
    print(x)
for x, y in a.items():
    print(x, y)
a["Nam sinh"] = 1999
print(a)
a.pop("Nam sinh")
print(a)
ban1 = {
    "ten": "javis",
    "tuoi": 19
}
ban2 = {
    "ten": "tony",
    "tuoi": 20
}
ban3 = {
    "ten": "stark",
    "tuoi": 13
}
lophoc = {
    "ban1": ban1,
    "ban2": ban2,
    "ban3": ban3
}
print(lophoc)


# Functions
def my_function():
    print("hello")


my_function()


def my_function(fname):
    print(fname + " Toan")


my_function("Do")
my_function("Nguyen")
my_function("Ngo")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Do", "Toan")


def key(a, b, c, d):
    print(a)
    print(b + 5, c)
    print(d)


A = [1, 2, 3, 4]
key(*A)


def mtd(be1, be2, be3):
    print("be lon nhat la be " + be1)


mtd("Toan", "huy", "TA")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Class and object
class Toan:
    x = 6


print(Toan)


class nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi


n1 = nguoi("Long", 20)
print(n1.ten)
print(n1.tuoi)


class nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def thongtin(self):
        print("tao ten la ", self.ten)


n1 = nguoi("Long", 20)
n1.thongtin()
