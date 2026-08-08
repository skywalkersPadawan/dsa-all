# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
in this problem have to parse through all of the sample input string and find out all of the valid css hex codes and print them to STDOUT

sample input:
    11
    #BED
    {
        color: #FfFdF8; background-color:#aef;
        font-size: 123px;
        background: -webkit-linear-gradient(top, #f9f9f9, #fff);
    }
    #Cab
    {
        background-color: #ABC;
        border: 2px dashed #fff;
    }

sample output:
    #FfFdF8
    #aef
    #f9f9f9
    #fff
    #ABC
    #fff

important part is the regex should exclude valid patterns like this
#BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.
"""

import re

N = int(input())
pattern = re.compile(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\b")

for _ in range(N):
    line = input()

    # Ignore CSS selector lines such as "#BED" or "#Cab"
    if line.strip().startswith("#"):
        continue

    for color in pattern.findall(line):
        print(color)
