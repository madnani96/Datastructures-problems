#Leetcode Link:https://leetcode.com/problems/isomorphic-strings/
def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dict={}
        for x in range(len(s)):
            if s[x] not in dict.keys() :
                dict[s[x]] = t[x]
                print(dict)
            elif(dict[s[x]] != t[x]):
                return False
            
        if len(dict.values()) != len(set(dict.values())):
            return False
        return True

#Input: s = "egg", t = "add"
#Output: true