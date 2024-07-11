import random

def create_number_random(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,100))
    return arr

def sort_insertion(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key

    print(i, '-', arr)

def main():
    n = int(input("Enter the number of elements: "))
    arr = create_number_random(n)
    print("arr 1",arr)
    sort_insertion(arr)
    print("arr 2", arr)

if __name__ == "__main__":
    main()