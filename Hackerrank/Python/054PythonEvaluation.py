# Enter your code here. Read input from STDIN. Print output to STDOUT

expression = input()
result = eval(expression)
if result is not None:
    print(result)


'''
Without the None check, print(eval(...)) also prints None when the
expression is a statement (e.g. print(2+3)). HackerRank uses plain
expressions, but we skip printing when eval returns None.

'''
