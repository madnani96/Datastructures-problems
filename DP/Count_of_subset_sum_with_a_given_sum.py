#Count of Subsets Sum with a Given Sum

#Given an array arr[] of length N and an integer X, 
#the task is to find the number of subsets with sum equal to X.

#https://www.youtube.com/watch?v=F7wqWbqYn9g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=9&ab_channel=AdityaVerma

import numpy as np

def memoizedsubsetsum(arr, length,sum, arr1):
        if sum == 0  :
            
            return 1
        
        if length ==0 and sum!=0:
            return 0
        
        if arr1[length][sum]!=-1:
            return arr1[length][sum]
        
        if arr[length-1]<=sum:
            arr1[length][sum] = (memoizedsubsetsum(arr,length-1,sum-arr[length-1],arr1) + (memoizedsubsetsum(arr, length-1, sum, arr1)))
            return arr1[length][sum]
        
        else:
            arr1[length][sum]= memoizedsubsetsum(arr, length-1,sum,  arr1)
            return  arr1[length][sum]
        



def memoizedsubsetsumfinal(arr,sum):
    length=len(arr)
    arr1= np.zeros((length+1,sum+1))
    arr1 =arr1.tolist()
    for i in range(length+1):
         for j in range(sum+1):
            arr1[i][j]=-1
    n = len(arr)
    return memoizedsubsetsum(arr,length,sum,arr1)





#print(memoizedsubsetsumfinal([2,3,5,6,4],1))
#print(memoizedsubsetsumfinal([1,2,3,3],6))
#print(memoizedsubsetsumfinal([4,2,4,2,2],10))


#arr = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]

#sum1 = sum(arr)//2
#print(memoizedsubsetsumfinal(arr,sum1))
#print(memoizedsubsetsumfinal(arr,197))

'''
TopDown approach
'''

def topdowncountofsubsetsumfinal(arr,sum):
    length=len(arr)
    arr1= np.zeros((length+1,sum+1))
    arr1 =arr1.tolist()
    for j in range(sum+1):
            arr1[0][j]=0

    for i in range(length+1):
        arr1[i][0] = 1      
    
    
    
    for i in range(1, length+1):
        for j in range( sum+1):
            if arr[i-1] <= j:
                arr1[i][j] = arr1[i-1][j-arr[i-1]] + arr1[i-1][j]
            else:
                arr1[i][j] = arr1[i-1][j]
    
    
    
    return arr1[i][j]
        
print(topdowncountofsubsetsumfinal([3, 34, 4, 12, 5, 2],7))


