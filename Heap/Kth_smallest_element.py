'''
Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

Example:
Input: arr[] = {7, 10, 4, 3, 20, 15}
k = 3
Output: 7 . 

'''

arr = [7, 10, 4, 3, 20, 15]
k=3
import heapq
def kthsmallest(arr,k):
    #newarr = [-x for x in arr]

    heapq.heapify(arr)

    for x in range(k):
        
        y = heapq.heappop(arr)
        if x == k-1:
            return y



print(kthsmallest(arr,k))