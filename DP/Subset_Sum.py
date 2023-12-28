#Ques: Given an array and value of n find a subset such that sum of subset is equal to n
'''
Recursive approach
'''
def subsetsum(arr, sum, length):
    if sum == 0:
        return True
    if length == 0 and sum != 0:
        return False
    
    
    if arr[length-1]<=sum:
        return (subsetsum(arr,sum-arr[length-1],length-1) or (subsetsum(arr, sum, length-1)))
    else:
        return subsetsum(arr, sum, length-1)




'''
Memoized approach
'''

import numpy as np

def memoizedsubsetsum(arr, length,sum, arr1):
        if sum == 0  :

            return True
        
        if length ==0 and sum!=0:
            return False
        
        if arr1[length][sum]!=-1:
            return arr1[length][sum]
        
        if arr[length-1]<=sum:
            arr1[length][sum] = (memoizedsubsetsum(arr,length-1,sum-arr[length-1],arr1) or (memoizedsubsetsum(arr, length-1, sum, arr1)))
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

arr = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]

sum1 = sum(arr)//2
print(memoizedsubsetsumfinal(arr,sum1))
print(memoizedsubsetsumfinal([3, 34, 4, 12, 5, 2],38))
#print(memoizedsubsetsumfinal(arr,197))
#arr=[10,7,8]
#print(memoizedsubsetsumfinal(arr,sum1))


'''
Top Down
'''
def topdownsubsetsumfinal(arr,sum):
    length=len(arr)
    arr1= np.zeros((length+1,sum+1))
    arr1 =arr1.tolist()
    for j in range(sum+1):
            arr1[0][j]=False

    for i in range(length+1):
        arr1[i][0] = True      
    
    
    
    for i in range(1, length+1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                arr1[i][j] = arr1[i-1][j-arr[i-1]] or arr1[i-1][j]
            else:
                arr1[i][j] = arr1[i-1][j]
    
    
    
    return arr1[i][j]
        
print(topdownsubsetsumfinal(arr,sum1))
        
print(topdownsubsetsumfinal([3, 34, 4, 12, 5, 2],79))