def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    lines = []

    # Upper half (including middle)
    for i in range(size):
        s = "-".join(alpha[size - 1 : i : -1] + alpha[i:size])
        width = 4 * size - 3
        lines.append(s.center(width, "-"))

    # Print full rangoli
    print("\n".join(lines[:0:-1] + lines))


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)


# solve this later
