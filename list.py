class abc:
    def __init__(self, list):
        self.list = list

    def insert(self):
        list.insert(self.list, 0, 2)
        print(self.list)

    def remove(self):
        list.remove(self.list, 6)
        print(self.list)

    def pop(self):
        list.pop(self.list,5)
        print(self.list)

    def clear(self):
        list.clear(self.list)
        print(self.list)

l1 = abc([1,2,3,4,5,6,7,8,9,10])
l1.insert()
l1.remove()
l1.pop()
l1.clear()

