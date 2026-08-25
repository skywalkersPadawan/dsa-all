# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
n_set = set(map(int, input().split()))
b = int(input())
b_set = set(map(int, input().split()))

intersection_set = n_set.intersection(b_set)
print(len(intersection_set))
