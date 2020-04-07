'''Ratiorg got statues of different sizes as a present from
CodeMaster for his birthday, each statue having an non-negative integer size.
Since he likes to make things perfect, he wants to arrange them from smallest
to largest so that each statue will be bigger than the previous one exactly by 1.
He may need some additional statues to be able to accomplish that.
Help him figure out the minimum number of additional statues needed.
'''


def makeArrayConsecutive2(*statues):
    dem = 0
    n = max(*statues)
    m = min(*statues)
    List_1 = []
    List_1.append(n)
    List_1.append(m)
    if len(*statues) == 1:
        return dem
    for x in range(1, n - m):
        y = min(*statues) + x
        List_1.append(y)
    Conse = list(set(List_1) - set(*statues))
    return (len(Conse))


print(makeArrayConsecutive2([2, 3, 8, 6]))
