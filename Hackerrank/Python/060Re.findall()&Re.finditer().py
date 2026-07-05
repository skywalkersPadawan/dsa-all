# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()
matches = re.findall(
    r'(?<=[qwrtypsdfghjklzxcvbnm])[aeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])', S, re.IGNORECASE)
# important read the rules of building regex expressions very carefully
# in this case (?<=...) is a positive lookbehind assertion that matches the pattern before the current position
# always solve regex expressions in small batches to build the final expression
if matches:
    for match in matches:
        print(match)
else:
    print(-1)
