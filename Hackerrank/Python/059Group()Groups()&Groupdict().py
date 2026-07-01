# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
S = input()
# re.search() will return the first ocurrence anywhere in the string, fairly easy to understand
match = re.search(r'([a-zA-Z0-9])\1+', S)
if match:
    print(match.group(1))
else:
    print(-1)
