# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, m = map(int, input().split())
lists = []
for _ in range(k):
    lists.append(list(map(int, input().split()))[1:])

print(max(sum(x * x for x in combination) % m for combination in product(*lists)))
