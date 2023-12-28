'''
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.

Example:

Input 1:
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
Output 1:
    C = [3, 3, 5, 5, 6, 7] . 

'''

arr = [1, 3, -1, -3, 5, 3, 6, 7]
arr = [3, 3, 5, 5, 6, 7]
k=3
maxlist=[]
maxlist.append(max(arr[:k]))
curentmax = max(arr[:k])

for x in range(k,len(arr)):
    if arr[x]>curentmax:
        maxlist.append(arr[x])
        curentmax = arr[x]
    else:
        maxlist.append(curentmax)

print(maxlist)