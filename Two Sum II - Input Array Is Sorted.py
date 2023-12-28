
'''
Leet Code Problem: Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''
numbers= [2,7,11,15]

target=9

x=0
y= len(numbers)-1
while((numbers[x]+numbers[y]) != target):
    temp = numbers[y]+numbers[x]
    if (temp > target):
        y-=1
    else:
        x+=1


print(x+1,y+1)








