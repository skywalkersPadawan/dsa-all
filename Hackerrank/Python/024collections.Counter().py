# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter


n = int(input())
sizes = Counter(map(int, input().split()))
customers = int(input())
total = 0

for _ in range(customers):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        sizes[size] -= 1
        total += price
print(total)
