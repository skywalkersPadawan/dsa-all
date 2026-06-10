# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    item_name, net_price = input().split()
    items[item_name] += int(net_price)

for item_name, net_price in items.items():
    print(item_name, net_price)


# all test cases failed study the library correctly and then solve the problem
# new items will face keyerrors if they are not initialized in the OrderedDict ValueError: too many values to unpack (expected 2)

'''
a simple explanation of the problem is 
line = "BANANA FRIES 12"
line.split()
will return ['BANANA', 'FRIES', '12']

that is the issue python cannot unpack 3 values into 2 variables New items will raise KeyError because they are not initialized in the OrderedDict. Also, item names may contain spaces, and that is why this will not work
'''
