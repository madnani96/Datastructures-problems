#https://leetcode.com/problems/is-subsequence/description/

s="abc"
t="ahbgdc"
lengthofs = len(s)
spointer = 0


for x in t:
    if(spointer != lengthofs):
        if x == s[spointer]:
            spointer+=1
        
if spointer == lengthofs:
    print(True)
else: 
    print(False)
        