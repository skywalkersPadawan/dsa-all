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

# previous commit was a test to see how cursor was tracking which lines are considered as AI completions the
"""
the following lines are tracked by cursor tab as AI completions which is correct when checked by cursor commit tracking AI completion lines


# time complexity: O(N)
# space complexity: O(1)
# memory usage: O(1)
# time complexity is O(N) because we are iterating through the input N times.
# space complexity is O(1) because we are not using any additional space.
# We use only a constant amount of extra space (the regex pattern and a few variables).
pattern = r'^[789]\d{9}$'

# 8th line that cursor was tracking as AI suggested tab completions not found in the commit (check later and test how this feature is working to check for licenses in proprietary code)
"""
