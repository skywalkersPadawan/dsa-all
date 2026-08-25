import re

pattern = re.compile(r"^[456]\d{3}(-?\d{4}){3}$")
for _ in range(int(input())):
    card = input()
    if not pattern.match(card):
        print("Invalid")
        continue

    digits = card.replace("-", "")
    if re.search(r"(\d)\1{3}", digits):
        print("Invalid")
    else:
        print("Valid")
