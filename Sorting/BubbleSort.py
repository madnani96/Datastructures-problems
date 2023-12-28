'''
Bubble Sort Algorithm
In this algorithm, traverse from left and compare adjacent elements and the 
higher one is placed at right side. 
In this way, the largest element is moved to the rightmost end at first. 
This process is then continued to find the second largest and place it 
and so on until the data is sorted.


'''

arr = [64, 34, 25, 12, 22, 11, 90]

def bubblesort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True

        if swapped == False:
            break
    return arr
print(bubblesort(arr))