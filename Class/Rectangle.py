class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def are(self):
        area = self.length * self.width
        print(area)


R1 = Rectangle(8, 11)
R1.are()
