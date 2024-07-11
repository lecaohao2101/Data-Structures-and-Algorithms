import random

def create_array_random(n):
    array = []
    for i in range(n):
        array.append(random.randint(0, 100))
    return array

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

def main():
    n = int(input("Enter the number of elements: "))
    arr = create_array_random(n)
    print("arr 1",arr)
    merge_sort(arr)
    print("arr 2", arr)

if __name__ == "__main__":
    main()