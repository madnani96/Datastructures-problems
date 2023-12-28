# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
nums = [1,2,2,2,3,4,5,5,5,6]

i = 0
j = 1
k = 2
print(nums)

while(k<len(nums)):
    if nums[i] == nums[j] and nums[j] == nums[k]:
        k+=1
    else:
        nums[j+1] = nums[k]
        k+=1
        j+=1
        i+=1



print(nums)

'''

i != j != k move fwd 
i==j != k  move fwd  nums[j+1]=nums[k]
i !=j j==k    move fwd

i==j==k increment k
'''