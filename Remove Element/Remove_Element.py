'''
Leet Code Problem: Remove Element
Link: https://leetcode.com/problems/remove-element
'''
https://leetcode.com/problems/remove-element
nums = [5,5,3,2,7,8,5]
val = 5
count = len(nums)
temp= len(nums)
i=0

while (i < temp):
    if (nums[i] == val):
        nums[i], nums[count-1]= nums[count-1], nums[i]
        count-=1
        temp-=1
    else:
        i+=1


nums=nums[0:count]
print(nums)
print(count)


