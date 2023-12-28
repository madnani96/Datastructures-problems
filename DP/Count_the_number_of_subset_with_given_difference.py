#

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
    countofzeros = 0
    for x in arr:
        if x==0:
            countofzeros+=1
    
    
    arr1= np.zeros((length+1,sum+1))
    arr1 =arr1.tolist()
    for i in range(length+1):
         for j in range(sum+1):
            arr1[i][j]=-1
    n = len(arr)
    return pow(2,countofzeros)*memoizedsubsetsum(arr,length,sum,arr1)







#print(memoizedsubsetsumfinal([2,3,5,6,4],1))
#print(memoizedsubsetsumfinal([1,2,3,3],6))
#print(memoizedsubsetsumfinal([4,2,4,2,2],10))

#S1+S2=sum
#S1-S2=diff
#S1=(sum+diff)/2
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
        

def countnumberofsubsetwithgivendifference(arr,difference):
    s1 = (sum(arr) + difference)//2
    
    #return memoizedsubsetsumfinal(arr,s1)
    #return pow(2,countofzeros)*topdowncountofsubsetsumfinal(arr,s1) 
    return topdowncountofsubsetsumfinal(arr,s1) 

#print(countnumberofsubsetwithgivendifference([1,1,2,3],1))
print(countnumberofsubsetwithgivendifference([0,1],1))


'''
table


'''



#[0,0,0,0,0,0,0,0,1]
#arr = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]

#sum1 = sum(arr)//2
#print(memoizedsubsetsumfinal(arr,sum1))
#print(memoizedsubsetsumfinal(arr,197))

'''
TWO REASONS FOR NOT GETTING ACCEPTED:
1)  We are initialising first column to 1, assuming there is only 1 way to make subset sum equal to 0,  i.e. null subset, BUT this fails if we have 0's as elements of array. If we have a single 0 present in the array, then the subsets will be '{}, {0}' whose sum will be 0. Hence, there can be more than 1 way to make sum==0.
FIX: Don't initialise the first col to be 1. Everything will be initialized to 0 except the first cell in the table i.e. dp[0][0]=1. AND j will start from 0 instead of 1.
2)  In the derived formula, target = (diff+totalSum) / 2, NOTICE that (diff+totalSum) must be even for target to be a whole number, else it's not possible to find a decimal target in subset sum. Hence, we also need to take care of the test cases where it's not possible to partition the array.
FIX: Check, if it's odd,  there is no way --> if((diff+totalSum)%2 != 0) return 0;

ACCEPTED CODE C++:
int countPartitions(int n, int d, vector<int>& arr) {
        int sum=0;
        for(auto i: arr) sum+=i;
        if((d+sum)%2 != 0) return 0;
        int t=(d+sum)/2;
        //REDUCED: find count of subset with sum equal to t
        vector<vector<int>> dp(n+1, vector<int>(t+1, 0));
        dp[0][0] = 1;
        for(int i=1; i<n+1; i++) {
            for(int j=0; j<t+1; j++) {
                if(arr[i-1] <= j) 
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-arr[i-1]])%1000000007;
                else
                    dp[i][j] = dp[i-1][j];
            }
        }
        return dp[n][t];
    }
'''