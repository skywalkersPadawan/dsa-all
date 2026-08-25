#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    return " ".join(word.capitalize() for word in s.split(" "))


# str capitalize() method is used to capitalize the first letter of each word in the string and then it also lowercases the rest of the letters in the word
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
