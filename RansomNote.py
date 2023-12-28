#link: https://leetcode.com/problems/ransom-note/
def canConstruct(ransomNote, magazine) :
        dict={}
        for x in magazine:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] = dict[x] + 1
        
        
        for x in ransomNote:
            if x not in dict:
                return False
            else: 
                temp = dict[x]
                if temp == 0:
                    return False
                else:
                    dict[x] = temp-1 
        return True
print(canConstruct("a", "ab"))