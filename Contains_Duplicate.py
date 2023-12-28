

'''
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] 
and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
''' 

nums = [1,2,3,1]
#nums = [1,0,1,1]
k = 3      
def containsNearbyDuplicate(nums, k) :
        dict={}
        
        for x in range(len(nums)):
            if nums[x] not in dict.keys():
                dict[nums[x]]=[x]
            else:
                dict[nums[x]].append(x)
        print(dict)
        for x in dict.keys():
             if len(dict[x])>1:
                  temp = dict[x] 
                  print(temp)
                  for y in range(len(temp)-1):
                        if abs(temp[y]-temp[y+1])<=k:
                            return True
        return False
        
print(containsNearbyDuplicate(nums,k))
