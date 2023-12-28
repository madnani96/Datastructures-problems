import numpy as np

def findTargetSumWays( nums, target) :
        
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
        


        def countnumberofsubsetwithgivendifference(arr,difference):
            s1 = (sum(arr) + difference)//2
            if sum(arr)<abs(difference):
                return 0
            if (difference + sum(arr)) % 2 != 0: 
                return 0

            return topdowncountofsubsetsumfinal(arr,s1) 
        return countnumberofsubsetwithgivendifference(nums, target)
        
print(findTargetSumWays([0,1], 1))