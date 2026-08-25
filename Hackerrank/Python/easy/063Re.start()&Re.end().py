# Enter your code here. Read input from STDIN. Print output to STDOUT

# import re

# S = input()
# k = input()

# # matches = re.finditer(k, S)
# matches = re.finditer(f"(?=({re.escape(k)}))", S)  # learn positive lookahead

# if matches:
#     for match in matches:
#         print((match.start(), match.start() + len(k) - 1))
#         # this will print the tuple in the format (start_index, end_index)
#         # read if the end_index matches the required output format for the test cases
# else:
#     print((-1, -1))


# 2 / 6 failing and match.end() has to be used to complete the problem

import re

S = input()
k = input()

# used to determine to print((-1, -1)) after the loop if match not found
found = False

for match in re.finditer(f"(?=({re.escape(k)}))", S):
    found = True
    start = match.start()
    end = start + len(k) - 1
    print((start, end))

if not found:
    print((-1, -1))
