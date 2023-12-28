def longestCommonPrefix(strs) :
        if len(strs) == 1:
            return strs[0]
        if len(set(strs))==1:
             return strs[0]


        max_len = -1
        for ele in strs:
            if len(ele) > max_len:
                max_len = len(ele)
                temp = ele
 
        



        lst=[]
        
        for x in range(0,len(temp)+1):
            lst.append(temp[:x])
        
        
        
        for x in range(1, len(lst)):
            for y in strs:
                if lst[x] not in y[: len(lst[x])]:
                    
                    return lst[x-1]
                    
            
        
        return ""



strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
#strs = ["flower","flower","flower","flower"]
#strs = ["aca","cba"]
strs = ["a","ac"]
print(longestCommonPrefix(strs))