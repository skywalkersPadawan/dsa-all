# Enter your code here. Read input from STDIN. Print output to STDOUT

N, x = map(int, input().split())

subject_scores = [list(map(float, input().split())) for _ in range(x)]
for student in zip(*subject_scores):
    print("{:.1f}".format(sum(student) / x))
