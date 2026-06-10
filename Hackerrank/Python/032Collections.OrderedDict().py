# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    item_name, net_price = input().split()
    items[item_name] += int(net_price)

for item_name, net_price in items.items():
    print(item_name, net_price)


# all the test cases failed study the lib correctly and then solve the problem
