# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except Exception as e:
        print("Error Code:", e)


# change the language server from python3 to pypy3 and run the code the test cases will pass
