# to print only valid email addresses from the input format (done using email parsing lib in python3 email.utils)# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from email.utils import parseaddr

n = int(input())
pattern = r"^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

for _ in range(n):
    line = input()
    name, address = line.split()
    parsed_name, parsed_email = parseaddr(address)

    if re.fullmatch(pattern, parsed_email):
        print(line)
