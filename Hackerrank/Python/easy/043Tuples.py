# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))

'''

the challenge is working in python 2 but not in python 3

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))


this will pass all the test cases

the hash values will differ between different versions of python and hackerrank's environment is passing only for python 2 python 3 hash value is not python 3 it is python 2 hash value
'''
