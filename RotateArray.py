nums = [1,2,3,4,5,6,7]
#https://leetcode.com/problems/rotate-array/description/
#nums = [-1, -100,3,99]
k = 3
#output = [5,6,7,1,2,3,4]
#k-=1




length = len(nums)
if length != 1:
    if(k<length):
        nums[:length-k], nums[-k:] = nums[-k:], nums[:length-k]
    else:
        while (k!=0):
            popelement = nums.pop()
            nums.insert(0,popelement)
            k-=1
#else:
    #return nums
    #do nothing
        