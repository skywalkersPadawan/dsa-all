# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

string, k = input().split()
k = int(k)

permutations = sorted(permutations(string, k))
for permutation in permutations:
    print("".join(permutation))
