#Leet Code Link:https://leetcode.com/problems/group-anagrams/description/
def groupAnagrams(self, strs):
        
        group = {}
        group["".join(sorted(strs[0]))] = [strs[0]]

        for x in range(1, len(strs)):
            temp = "".join(sorted(strs[x]))
            
            if temp in group.keys():
                group[temp].append(strs[x])
            else:
                group[temp] = [strs[x]]
        return group.values()

#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
