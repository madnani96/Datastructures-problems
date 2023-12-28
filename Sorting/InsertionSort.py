'''
Insertion sort is a simple sorting algorithm that works similar to the way 
you sort playing cards in your hands. The array is virtually split into a sorted and an 
unsorted part. Values from the unsorted part are picked and placed at the correct position 
in the sorted part.

'''

arr = [64, 34, 25, 12, 22, 11, 90]
def insertion_sort(arr):


    for i in range(len(arr)):
   
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort(arr))