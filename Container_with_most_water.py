#Link: https://leetcode.com/problems/container-with-most-water/description/
height = [1,8,6,2,5,4,8,3,7]
#ans =49
height = [1,3,2,5,25,24,5]
#ans = 24

i = 0
j = len(height)-1
maxarea = (j-i)*min(height[j],height[i])


        
for x in range(len(height)-1):
            
    if height[i]>height[j]:
        j-=1
        maxarea = max(maxarea, (j-i)* min(height[j],height[i])) 
    else:
        i+=1
        maxarea = max(maxarea, (j-i)* min(height[j],height[i]))

print(maxarea)
'''
#print(maxarea)
length = len(height)
i = 0
maxarea = 0
for i in range(len(height)):
    for j in range(i+1,len(height)):
        maxarea=  max(maxarea, (j-i)*min(height[j],height[i]))

print(maxarea)


'''