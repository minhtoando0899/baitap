# # Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
# def prime_eratosthenes(n):
#     prime_list = []
#     for i in range(2, n+1):
#         if i not in prime_list:
#             print (i)
#             for j in range(i*i, n+1, i):
#                 prime_list.append(j)
#
# print(prime_eratosthenes(100))
class Prime_eratosthenes:
    def __init__(self, list):
        self.list = list
        self.list_1 = []

    def prer(self):
        for i in range(2, len(self.list) + 1):
            if i not in self.list_1:
                print(i)
                for j in range(i * i, len(self.list) + 1, i):
                    self.list_1.append(j)


P1 = Prime_eratosthenes(range(100))
P1.prer()
