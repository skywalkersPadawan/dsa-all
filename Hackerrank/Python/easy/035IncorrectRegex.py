# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)


'''

this is the python 2 version of the code —> pypy3 will not work because hackerrank has not updated the python 3 test cases to work with newer regex mutations that are used in python 3.10+

import re

for _ in xrange(int(raw_input())):
    try:
        re.compile(raw_input())
        print True
    except re.error:
        print False


this code will pass all the test cases        
'''
