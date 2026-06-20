# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())  # the number of test cases


for _ in range(T):
    _ = int(input())
    A = set(map(int, input().split()))
    _ = int(input())
    B = set(map(int, input().split()))
    if A.issubset(B):
        print(True)
    else:
        print(False)
