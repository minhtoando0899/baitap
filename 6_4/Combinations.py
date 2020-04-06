# # Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list.
# def combination(n, n_list):
#     if n<=0:
#         yield []
#         return
#     for i in range(len(n_list)):
#         c_num = n_list[i:i+1]
#         for a_num in combination(n-1, n_list[i+1:]):
#             yield c_num + a_num
# n_list = [1,2,3,4,5,6,7,8,9]
# print("Original list:")
# print(n_list)
# n = 2
# result = combination(n, n_list)
# print("\nCombinations of",n,"distinct objects:")
# for e in result:
#      print(e)
class Combinations:
    def __init__(self, n, list):
        self.list = list
        self.n = n

    def com(self):
        if self.n <= 0:
            yield []
            return
        for i in range(len(self.list)):
            c_num = self.list[i:i + 1]
            for a_num in Combinations(self.n - 1, self.list[i + 1:]):
                yield c_num + a_num
                return


C1 = Combinations(2, [1, 2, 3, 4, 5, 6, 7, 8, 9])
C1.com()
print("Original list:")
print(C1.list)
n = 2
print("Combinations of", n, "distinct objects:")
print(C1.com())
