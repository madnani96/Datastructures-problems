'''
def word(s,wordDict):
            
            if s in wordDict or len(s)==0:
                return True
            
            for k in range(1,len(s)):
                temp = word(s[0:k],wordDict) and word(s[k:],wordDict)
                if temp:
                       return True
            return False

s = "leetcode"
wordDict = ["leet","code"]


#s = "catsandog"
#wordDict = ["cats","dog","sand","and","cat"]

print(word(s,wordDict))


'''
s = "leetcode"
wordDict = ["leet","code"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

def word(s,wordDict,dp,i,j):
            
    if s[i:j+1] in wordDict or len(s)==0:
        return True
            
    if dp[i][j]!=-1:
        return dp[i][j]


    for k in range(i,j):
        temp = word(s,wordDict,dp,i,k) and word(s,wordDict,dp,k+1,j)
        dp[i][j] = temp
        if temp:
            return True
    return False
        
        
dp=[[-1]*len(s) for x in range(len(s))]
        
print(word(s,wordDict,dp,0,len(s)-1))
