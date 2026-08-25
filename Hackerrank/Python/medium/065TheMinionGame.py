def minion_game(string):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    kevin = 0
    stuart = 0
    n = len(string)

    for i, ch in enumerate(string):
        if ch in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

# first pass solve


if __name__ == '__main__':
    s = input()
    minion_game(s)
