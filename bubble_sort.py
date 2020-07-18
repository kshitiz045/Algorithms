#Developed By : Kshitiz Gupta
# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = input("Enter the elements").split()
bubbleSort(arr)
print('Sorted list: ', end='')
print(arr)
