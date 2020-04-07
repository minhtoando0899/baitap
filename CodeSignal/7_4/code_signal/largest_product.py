# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
def adjacentElementsProduct(inputArray):
    max = (inputArray[0] * inputArray[1])
    for x in range(1, len(inputArray) - 1):
        if (inputArray[x] * inputArray[x + 1]) > max:
            max = (inputArray[x] * inputArray[x + 1])
    return max
print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))