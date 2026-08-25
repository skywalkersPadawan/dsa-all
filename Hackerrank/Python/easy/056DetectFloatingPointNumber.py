# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for _ in range(T):
    s = input()
    try:
        value = float(s)
        if s.strip() in ['.', '+.', '-.', '+', '-']:
            print(False)
            continue
        parts = s.split('.')
        if len(parts) == 2:
            left, right = parts
            if (left.strip("+-") == '' and right == ''):
                print(False)
                continue
            if left.strip("+-") == '' and right.isdigit():
                print(True)
                continue
            if left.lstrip("+-").isdigit() and (right == '' or right.isdigit()):
                print(True)
                continue
            print(False)
        else:
            # If there's no dot, not a floating point number
            print(False)
    except ValueError:
        print(False)


# do not validate the format of the input using regex because float directly handles the cases that hackerrank considers valid for the test cases to pass

''' this fails because 0 is an integer but 0.0 is a floating point number  and number = float(input()) will return true for 0 and 0.0 but that will fail the hackerrank test case '''

# this solution is wrong because test cases are not properly understood

# revisit this problem later currently this is solved with help from chatgpt
