# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = int(input())  # size of A, not needed
A = set(map(int, input().split()))

# number of other sets
n = int(input())
for _ in range(n):
    command = input().split()
    B = set(map(int, input().split()))
    if command[0] == 'intersection_update':
        A.intersection_update(B)
    elif command[0] == 'update':
        A.update(B)
    elif command[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif command[0] == 'difference_update':
        A.difference_update(B)
print(sum(A))
