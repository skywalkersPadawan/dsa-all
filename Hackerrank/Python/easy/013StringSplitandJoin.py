def split_and_join(line):
    # write your code here
    # split the string on a " " (space) and then join using a delimiter "-"
    return "-".join(line.split(" "))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
