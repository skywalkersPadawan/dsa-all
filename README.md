# dsa-all

Repository for DSA solutions from LeetCode, HackerRank, and HackerEarth. Initial commits include previously solved problems, followed by new solutions and ongoing practice.

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

- Print all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n.
- Use list comprehensions instead of multiple loops, as a learning exercise.
  for the given example of
  x = 1
  y = 1
  z = 2
  the ranges are:
  i -> 0, 1 (2 values)
  j -> 0, 1 (2 values)
  k -> 0, 1, 2 (3 values)
  Total combinations:
  2 x 2 x 3 = 12

  So there are 12 total triplets before filtering.

  [0,0,0]
  [0,0,1]
  [0,0,2]

  [0,1,0]
  [0,1,1]
  [0,1,2]

  [1,0,0]
  [1,0,1]
  [1,0,2]

  [1,1,0]
  [1,1,1]
  [1,1,2]

  Then remove the ones where:
  i + j + k == 3
  [0,1,2]
  [1,0,2]
  [1,1,1]

  So the final list is:
  [0,0,0]
  [0,0,1]
  [0,1,0]
  [1,0,0]
  [1,0,1]
  [1,1,0]

  ```python
  if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    # this will be completed later
  ```
