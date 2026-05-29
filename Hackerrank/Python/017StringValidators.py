if __name__ == '__main__':
    s = input()
    # check if the string is alphanumeric
    print(any(char.isalnum() for char in s))
    # check if the string is alphabetical
    print(any(char.isalpha() for char in s))
    # check if the string is digits
    print(any(char.isdigit() for char in s))
    # check if the string is lowercase
    print(any(char.islower() for char in s))
    # check if the string is uppercase
    print(any(char.isupper() for char in s))
