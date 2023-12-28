'''
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.

Example:

Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr3  + Arr4 =700,
which is maximum. . 
'''
k=2
arr=[100,200,300,400]
sum=0
for x in range(k):
    sum+=arr[x]
arr2=[sum]
for x in range(k,len(arr)):
    sum = sum-arr[x-k]+arr[x]
    arr2.append(sum)
print(max(arr2))

