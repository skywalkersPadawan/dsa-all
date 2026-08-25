# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

N, M = map(int, input().split())
arr = numpy.array([input().split() for _ in range(N)], int)
print(numpy.transpose(arr))
print(arr.flatten())
