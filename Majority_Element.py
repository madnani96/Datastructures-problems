#https://leetcode.com/problems/majority-element/description/
nums = [2,2,1,1,1,2,2]

candidateelement=nums[0]
count = 1
for x in range(1 , len(nums)):
    if nums[x] != candidateelement:
        count-=1
    else:
        count+=1
    if count == 0:
        candidateelement = nums[x]
        count = 1

#return candidateelement

