# Given the string, check if it is a palindrome.

def checkPalindrome(inputString):
    if (inputString == inputString[::-1]):
        return True
    else:
        return False


print(checkPalindrome('aasbbsaa'))
print(checkPalindrome('asdasd'))
