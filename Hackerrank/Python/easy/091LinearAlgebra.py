import numpy

n = int(input())
matrix = numpy.array([input().split() for _ in range(n)], float)
print(round(numpy.linalg.det(matrix), 2))
