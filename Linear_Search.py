import random

def create_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 100))
    return arr

def find_linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def main():
    n = int(input("Enter the number of elements: "))
    arr = create_array(n)
    print("Array:", arr)
    x = int(input("Enter the element to search: "))
    index = find_linear_search(arr, x)
    if index == -1:
        print("Element not found")
    else:
        print("Element found at index", index)

if __name__ == "__main__":
    main()