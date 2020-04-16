# Write a Python program to implement pow(x, n).
class Pow:
    def pow(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        if n == 0:
            return 1
        if n < 0:
            return 1 / self.pow(x, -n)
        val = self.pow(x, n // 2)
        if n % 2 == 0:
            return val * val
        return val * val * x


print(Pow().pow(5, 10))
print(Pow().pow(2, -3))
print(Pow().pow(30, 0))
