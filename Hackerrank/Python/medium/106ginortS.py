# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

print(
    "".join(
        sorted(
            s,
            key=lambda c: (
                0 if c.islower() else 1 if c.isupper() else 2 if int(c) % 2 else 3,
                c,
            ),
        )
    )
)
