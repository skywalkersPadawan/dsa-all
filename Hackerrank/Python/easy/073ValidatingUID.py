# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_valid(uid):
    if len(uid) != 10:
        return False

    if not uid.isalnum():
        return False

    uppercase_count = 0
    digit_count = 0
    for char in uid:
        if char.isupper():
            uppercase_count += 1

        if char.isdigit():
            digit_count += 1

    if uppercase_count < 2:
        return False

    if digit_count < 3:
        return False

    if len(set(uid)) != 10:
        return False

    return True


for _ in range(int(input())):
    uid = input()
    if is_valid(uid):
        print("Valid")
    else:
        print("Invalid")
