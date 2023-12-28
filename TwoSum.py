#Link:https://leetcode.com/problems/two-sum/
def twoSum(nums, target) :
        dict={}
        for x in range(len(nums)):
            
                temp = target - nums[x]
                if temp in dict.keys():
                    print(dict)
                    return [x , dict[temp]]
                else:
                    dict[nums[x]] = x
            
                
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]