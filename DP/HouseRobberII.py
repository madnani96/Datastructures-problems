#leetcode link: 

def rob( nums) :
        #either ignore the first element or ignore last element run rob1 two times and take the max of it
        
        def rob1(nums):        
            length = len(nums)
            if length==2:
                return max(nums[0],nums[1])
            
            elif length>2:
                dp = [-2]*length
                dp[0] = nums[0]
                dp[1] =max(nums[0],nums[1])
            
            for i in range(2, length):
                dp[i] = max(nums[i]+ dp[i-2], dp[i-1])
                
            return dp[length-1]
        
        
        if len(nums)==1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif len(nums) == 3:
            return max(max(nums[0],nums[1]), max(nums[1],nums[2]))
        else:
            return max(rob1(nums[:len(nums)-1]), rob1(nums[1:]))
