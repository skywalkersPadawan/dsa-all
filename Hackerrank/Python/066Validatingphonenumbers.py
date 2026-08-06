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

# first pass solve
# time complexity: O(N)
# space complexity: O(1)
# memory usage: O(1)
# time complexity is O(N) because we are iterating through the input N times.
# space complexity is O(1) because we are not using any additional space.
# We use only a constant amount of extra space (the regex pattern and a few variables).
