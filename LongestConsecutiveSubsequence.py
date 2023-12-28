#Link: https://leetcode.com/problems/longest-consecutive-sequence/description/


def longestConsecutive( nums) :

        if len(nums) == 0:
            return 0
        nums = set(nums)
        
        test = 1
        longest = 1
        for x in nums:
            temp = x 
            if (x-1 not in nums):
                while(temp + 1 in nums):
                    temp+=1    
            longest = max(temp-x+1, longest)
        return longest

'''
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''