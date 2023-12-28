import numpy as np
#https://leetcode.com/problems/partition-equal-subset-sum/description/
    
def canPartition(nums) :
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

        
        if sum(nums)%2!=0:
            return False
        else:
            return memoizedsubsetsumfinal(nums,sum(nums)//2)


print(canPartition([1,2,5,2]))
        
    