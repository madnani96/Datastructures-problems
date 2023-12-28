'''
Sum of subset differences
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference 
between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements, 
Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example:
Input:  arr[] = {6, 14, 5,1} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 
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



def minimumsubsetdifference(arr):
        sum1=sum(arr)
        x=0
        y=0
        count=2
        final=[]
        for i in range (0 ,sum1//2+1):
            if memoizedsubsetsumfinal(arr,i):
                
                final.append(i)
        
        minimum=999999
        print(final)
        for x in final:
            minimum = min((sum1-2*x), minimum)
        return minimum
                
print("ss")
print(minimumsubsetdifference([1,4,5]))



def topdownsubsetsumfinal(arr):
    sum2= sum(arr)
    length=len(arr)
    arr1= np.zeros((length+1,sum2+1))
    arr1 =arr1.tolist()
    for j in range(sum2+1):
            arr1[0][j]=False

    for i in range(length+1):
        arr1[i][0] = True      
    for i in range(1, length+1):
        for j in range(1, sum2+1):
            if arr[i-1] <= j:
                arr1[i][j] = arr1[i-1][j-arr[i-1]] or arr1[i-1][j]
            else:
                arr1[i][j] = arr1[i-1][j]
    
    
    
    
    minimum=999999
    for k in range (0 ,sum2//2+1):        
        if arr1[length][k]==True:
            minimum = min((sum2-2*k), minimum)
            
    #print(final,"test")
    
    
    return minimum
    
print(topdownsubsetsumfinal([1,4,5]))