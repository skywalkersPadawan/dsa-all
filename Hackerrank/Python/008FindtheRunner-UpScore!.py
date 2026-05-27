if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])
    # to find the second highest score or the runner up score this is the fastest way to do it

# this might not be the best approach for interviews
# below solution is algorithmically more efficient in terms of time complexity and asymptotically faster than the first solution
'''
first = second = float('-inf')
for n in arr:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n
print(second)

'''
