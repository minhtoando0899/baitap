'''Given a year, return the century it is in. The first century spans
from the year 1 up to and including the year 100,
 the second - from the year 101 up to and including the year 200, etc.'''


def centuryFromYear(year):
    century = 0
    if year > 0:
        if year % 100 == 0:
            century += year / 100
        if year % 100 != 0:
            century += (year // 100) + 1
        return century


print(centuryFromYear(1999))


# CÁCH 2
def centuryFromYear(year):
    if year > 0:
        return int((year - 1) / 100 + 1)


print(centuryFromYear(2001))
