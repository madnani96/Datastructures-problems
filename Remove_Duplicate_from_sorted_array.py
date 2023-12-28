#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


nums = [1,2,2,2,3,4,5,5,6]

i = 0
j=1
print(nums)

while (j< len(nums)):
    if nums[i] != nums[j]:
        nums[i+1] = nums[j]
        i+=1
        j+=1
    else:
        j+=1


print(nums)