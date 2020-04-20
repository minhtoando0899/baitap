class Count:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1


if __name__ == '__main__':
    a, b = 1, 10
    c1 = Count(a, b)
    obj = iter(c1)
    try:
        while True:
            print("kill more, knock out: ", next(obj))
    except:
        print("you win")
