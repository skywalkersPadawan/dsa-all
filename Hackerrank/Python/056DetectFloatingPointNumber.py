# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for _ in range(T):
    # verify if the input is a floating point number from the given rules
    try:
        number = float(input())
        print(True)
    except ValueError:
        print(False)


# do not validate the format of the input using regex because float directly handles the cases that hackerrank considers valid for the test cases to pass

''' this fails because 0 is an integer but 0.0 is a floating point number  and number = float(input()) will return true for 0 and 0.0 but that will fail the hackerrank test case '''

# this solution is wrong because test cases are not properly understood
