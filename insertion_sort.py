#Developed By Kshitiz Gupta
#Python program for implementation of Insertion Sort

def insertion_sort(num):
    for i in range(1 , len(num)):
        key = num[i]
        j = i-1
        while (j>=0 and num[j]>key ):
            num[j+1]=num[j]
            j=j-1
        num[j+1]=key

num = input("Enter the elements ").split()
insertion_sort(num)
print('Sorted list are : ', end='')
print(num)
