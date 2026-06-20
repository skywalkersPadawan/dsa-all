# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
from collections import Counter
n = int(input())
rooms = list(map(int, input().split()))

# need to find the captain's room
# the captain's room will be the room that appears only once in the list
# we can use a set to find the room that appears only once
captain_room = set(rooms)
for room in captain_room:
    if rooms.count(room) == 1:  # this will be O(n^2) time complexity
        print(room)

# time limit exceeded need to to try a mathematical approach, the time complexity is O(n^2) which will not pass for this challenge


# alternative approach use Counter from collections module

'''
from collections import Counter
n = int(input())
rooms = list(map(int, input().split()))

rooms_counter = Counter(rooms)
for room, count in rooms_counter.items():
    if count == 1:
        print(room)
        break
# this will be O(n) time complexity
