def wrapper(f):
    def fun(l):
        # complete the function
        formatted_numbers = []
        for number in l:
            number = number[-10:]
            formatted_numbers.append(f"+91 {number[:5]} {number[5:]}")

        f(formatted_numbers)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep="\n")


if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
