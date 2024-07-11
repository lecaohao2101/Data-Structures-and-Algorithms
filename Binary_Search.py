import random

def create_array_ascending(n):
    arr = []
    number_first = random.randint(-100, 100)
    arr.append(number_first)
    for i in range(1, n):
        ascending = random.randint(0, 10)
        number = arr[i-1]+ascending
        arr.append(number)
    return arr

def find_binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    n = int(input("Enter the number of elements: "))
    arr = create_array_ascending(n)
    print(arr)
    x = int(input("Enter the element to search: "))
    result = find_binary_search(arr, x)
    if result == -1:
        print("Element not found")
    else:
        print("Element found at index", result)

if __name__ == "__main__":
    main()