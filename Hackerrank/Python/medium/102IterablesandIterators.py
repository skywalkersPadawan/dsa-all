from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())
total = list(combinations(letters, k))
count = sum("a" in comb for comb in total)
print(count / len(total))
