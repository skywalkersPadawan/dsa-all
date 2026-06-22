# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
numbers = list(map(int, input().split()))

print(all(x > 0 for x in numbers) and any(
    str(x) == str(x)[::-1] for x in numbers))


# converting to list of integers and then converting back to string and then checking for palindromic number 😅 (bad) and then the hidden test case was failing because the numbers were not integers I am not dumb infact 😅
