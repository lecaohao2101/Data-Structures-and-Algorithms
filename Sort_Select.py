import random

def create_array_random(n):
    array = []
    for i in range(n):
        array.append(random.randint(0, 100))
    return array

def sort_select(array):
    n = len(array)
    for i in range(n):
        index_min = i
        for j in range(i+1, n):
            if array[j] < array[index_min]:
                index_min = j
        array[i], array[index_min] = array[index_min], array[i]
        # print(i+1, "-", array)

def main():
    array = create_array_random(10)
    print("array 1",array)
    sort_select(array)
    print("array 2", array)

if __name__ == "__main__":
    main()