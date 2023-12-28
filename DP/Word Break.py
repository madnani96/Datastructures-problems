'''
my approach only better than 5% people
'''
def wordBreak(s, wordDict):
        
        def word(s,dp,i,j):
            
            if dp[i][j]!=-1:
                return dp[i][j]

            if s[i:j+1] in wordDict or len(s)==0:
                return True
                    
            for k in range(i,j):
                dp[i][j] = word(s,dp,i,k) and word(s,dp,k+1,j)
                if dp[i][j]:
                    return True
            return False

        dp=[[-1]*len(s) for x in range(len(s))]
        
        return word(s,dp,0,len(s)-1)

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordBreak(s,wordDict))



'''new approach

70% better
'''

def word(s,dp,i,j):
            if len(s[i:j])==0:
                return True

            if dp[i]!=-1:
                return dp[i]
                    
            for k in range(i,j):
                if s[i:k+1] in wordDict and word(s,dp,k+1,j):
                        dp[i] =True
                        return dp[i]
            dp[i] = False
            return dp[i]

dp = [-1]*len(s)
print(word(s,dp,0,len(s)))
       