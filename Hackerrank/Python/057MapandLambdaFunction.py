def cube(x): return x**3  # complete the lambda function


def fibonacci(N: int) -> list[int]:
    # return a list of fibonacci numbers
    fib = []
    n1, n2 = 0, 1

    for _ in range(N):
        fib.append(n1)
        n1, n2 = n2, n1 + n2
    return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
