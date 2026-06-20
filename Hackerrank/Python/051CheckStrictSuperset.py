# Enter your code here. Read input from STDIN. Print output to STDOUT


A = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    B = set(map(int, input().split()))
    if not B < A:
        print(False)
        break
else:
    print(True)
