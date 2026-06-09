def average(array):
    # your code goes here
    set_array = set(array)
    # the height should be 3 decimal places and should have only the unique elements in the array for the average calculation
    average = sum(set_array) / len(set_array)
    return round(average, 3)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
