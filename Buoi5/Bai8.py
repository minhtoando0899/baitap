# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))
class Long_words:
    def __init__(self, n, string):
        self.n = n
        self.string = string.split(" ")
        self.words_len = []

    def Lwords(self):
        for x in self.string:
            if len(x) > self.n:
                self.words_len.append(x)


l1 = Long_words(3, "The quick brown fox jumps over the lazy dog")
l1.Lwords()
print(l1.words_len)
