
#Python program for the implementation of selection sort

arr = ['p' , 'y' , 't' , 'h' , 'o' , 'n']
for i in range(len(arr)):
   min_ar= i
   for j in range(i+1, len(arr)):
      if arr[min_ar] > arr[j]:
         min_ar = j

arr[i], arr[min_ar] = arr[min_ar], arr[i]

for i in range(len(arr)):
   print(arr[i])
