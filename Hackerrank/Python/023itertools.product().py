# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools


def product(a, b):
    return " ".join(map(str, list(itertools.product(a, b))))
# itertools.product() is used to generate the cartesian product of two lists and then we join the result with a space separator


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(product(a, b))
