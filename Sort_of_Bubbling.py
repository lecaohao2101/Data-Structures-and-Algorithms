import random

def create_array_random(n):
    arr = []

    for i in range(n):
        number_random = random.randint(0, 100)
        arr.append(number_random)
    return arr

def sort_bubble(arr):
    n = len(arr)

    for i in range(n):
        continues = False
        for j in range(n-2, i-1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                continues = True
        # print(i+1, "-", arr)

        if continues == False:
            break

def main():
    n = int(input("Enter the number of elements: "))
    arr = create_array_random(n)
    print("arr 1",arr)
    sort_bubble(arr)
    print("arr 2", arr)

if __name__ == "__main__":
    main()