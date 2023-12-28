'''
Leet Code Problem: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
'''

nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
#nums1 = [2,0]
#nums2 =[1]
m=3
n=3
index = 0

#1,2,3,4,0,0,0
#2,5,6
i = m-1
j = n-1
k = m+n-1 


while(j>=0):
    if ((nums1[i]>nums2[j]) and (i>=0)):
        nums1[k]=nums1[i]
        i-=1
        k-=1
        
    else:
        nums1[k] = nums2[j]
        j-=1
        k-=1
        

print(nums1)

