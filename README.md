# dsa-all

Repository for DSA solutions from LeetCode, HackerRank, HackerEarth, and GeeksforGeeks. Initial commits include previously solved problems, followed by new solutions and ongoing practice.

##### 001hello_world.py

- Print "Hello, World!" to the console.

```python
if __name__ == "__main__":
    print("Hello, World!")
```

##### 002PythonIf-Else.py

- Print "Weird" if the number is odd, "Not Weird" if the number is even and greater than 20, "Weird" if the number is even and between 6 and 20, "Not Weird" if the number is even and less than 6.

```python
if __name__ == "__main__":
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
```

##### 003ArithmeticOperators.py

- Print the sum, difference, and product of two numbers.

```python
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)
```

##### 004PythonDivision.py

- Print the quotient and division of two numbers.

```python
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)
```

##### 005Loops.py

- Print the squares of the first n natural numbers.

```python
if __name__ == "__main__":
    n = int(input())
    for i in range(0, n):
        print(i**2)
```

##### 006PrintFunction.py

- Print the numbers from 1 to n separated by a space.

```python
if __name__ == "__main__":
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")
```

##### 007ListComprehensions.py
