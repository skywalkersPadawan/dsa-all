# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = map(int, input().split())
A = defaultdict(list)
# B = defaultdict(list) # this is not required at all there is no need to store any B values
B = []

for i in range(n):
    A[input()].append(i + 1)

# for i in range(m):
#     B[input()].append(i + 1) this has to converted to a list of strings or just process all of the values of A in the same loop only group A needs it's position to be tracked

for _ in range(m):
    B.append(input())

for word in B:
    if word in A:
        # this is the standard convention for printing a list of values with a space separator
        print(*A[word])
    else:
        print(-1)
