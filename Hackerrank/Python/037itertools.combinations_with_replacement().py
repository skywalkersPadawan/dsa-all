# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

string, k = input().split()
for i in combinations_with_replacement(sorted(string), int(k)):
    print("".join(i))
