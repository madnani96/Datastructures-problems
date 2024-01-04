#https://leetcode.com/problems/3sum/description/
#https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/
def threeSum(self, nums) :
        
        
        set1=set()
        for i in range(len(nums)):
            set2=set()
            for j in range(i+1,len(nums)):
                third = -(nums[i]+nums[j])
                if third in set2:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    set1.add(tuple(temp))
                
                set2.add(nums[j])
        return set1
    

#more optimal approach

def three3Sum(nums):
        nums.sort()
        finalset = set()
        length=len(nums)
        for i in range(length-2):
            j=i+1
            k= len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k] == 0:
                    finalset.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif (nums[i]+nums[j]+nums[k]) > 0:
                    k-=1
                else:
                    j+=1
        return list(finalset)

nums = [-1,0,1,2,-1,-4]
print(three3Sum(nums))


#another approach

def threesum(nums):

        nums.sort()
        finalset = []
        length=len(nums)
        for i in range(length-2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j=i+1
            k= len(nums)-1
            while(j<k):
                total = nums[i]+nums[j]+nums[k]
                
                if total > 0:
                    k-=1
                elif total < 0:
                    j+=1
                else:
                    finalset.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1

        return finalset
         