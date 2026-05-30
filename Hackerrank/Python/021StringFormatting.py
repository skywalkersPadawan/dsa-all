def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        # convert hexadecimal to uppercase this is the reason the test case was failing before
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


''' 
a more pythonic way to solve this problem is to use the format method with the width specifier.
def print_formatted(number):
    width = len(f"{number:b}")
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")
   
'''
