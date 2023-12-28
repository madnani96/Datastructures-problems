def houserobber(nums, n, lastrobbed):

            if n==0:
                return 0
            
            if lastrobbed == -1:
                return max(nums[n-1]+houserobber(nums, n-1, n-1), houserobber(nums, n-1, lastrobbed))
            
            if n == lastrobbed:
                return (houserobber(nums, n-1, lastrobbed))
            else:
                return max(nums[n-1]+houserobber(nums, n-1, n-1), houserobber(nums, n-1, lastrobbed))
             
nums = [2,7,9,3,1]   
nums = [2, 7,3,1,4,2,1,8]     
print(houserobber(nums, len(nums),-1))

def houserobber1(nums, n):

            if n==0:
                return nums[0]
            if n<0:
                return 0
            

            return max(nums[n]+houserobber1(nums, n-2), houserobber1(nums, n-1))
            
    
print(houserobber1(nums, len(nums)-1))          
             


def memoizedhouserobber(nums, n, dp):

        if n==0:
            return nums[0]
        if n<0:
            return 0
        if dp[n]!=-2:
            return dp[n]  
        else:    
            dp[n] = max(nums[n]+memoizedhouserobber(nums, n-2, dp), memoizedhouserobber(nums, n-1, dp))
            return dp[n]

def memoizedhouserobberfinal(nums,n):
      
    dp = [-2]*len(nums)
    return memoizedhouserobber(nums,n,dp)
      
print(memoizedhouserobberfinal(nums,len(nums)-1))



        


nums = [2, 7,3,1,4,2,1,8]           
def memoizedhouserobber1(nums,n):
      
    dp = [-2]*len(nums)
    if len(nums)>2:
        dp[0]= nums[0]
        dp[1] =max(nums[0],nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(nums[i]+ dp[i-2], dp[i-1])
    
    return dp[n]
      
print(memoizedhouserobber1(nums,len(nums)-1))