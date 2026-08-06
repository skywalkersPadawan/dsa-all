# Enter your code here. Read input from STDIN and print output to STDOUT
import re

pattern = r'^[789]\d{9}$'
N = int(input())

for _ in range(N):
    phone = input()
    if re.match(pattern, phone):
        print("YES")
    else:
        print("NO")
