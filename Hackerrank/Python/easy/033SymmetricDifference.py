# Enter your code here. Read input from STDIN. Print output to STDOUT


m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

symmetric_difference = m_set.symmetric_difference(n_set)
for i in sorted(symmetric_difference):
    print(i)


# very easy and straighforward problem just use the symmetric_difference method to find the symmetric difference between the two sets and then print the sorted values
