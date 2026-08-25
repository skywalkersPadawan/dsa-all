# Enter your code here. Read input from STDIN. Print output to STDOUTfrom
# the challenge is to use the namedtuple and solve the problem in 4 lines or lesser

from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())
total = 0
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)
print(total / n)
