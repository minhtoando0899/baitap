# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
def shapeArea(n):
    tarea = (n ** 2 + (n - 1) ** 2)
    return tarea
print(shapeArea(6))