'''
https://www.youtube.com/watch?v=4Urd0a0BNng&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=20
'''


def longestcommonsubsequence(str1,str2,l1,l2):
    if l1==0 or l2==0:
        return 0
    
    if str1[l1-1] == str2[l2-1]:
        return 1 + longestcommonsubsequence(str1,str2,l1-1,l2-1)
    
    else:
        return max(longestcommonsubsequence(str1,str2,l1-1,l2),longestcommonsubsequence(str1,str2,l1,l2-1))
    
#print(longestcommonsubsequence("ab","ab",2,2))
#print(longestcommonsubsequence("abcdgh","abedfhr",6,7))


'''
memoized

'''

def memoizedlongestcommonsubsequencefinal(str1,str2,l1,l2,dp):
    if l1==0 or l2==0:
        return 0
    
    if dp[l1][l2]!=-1:
        return dp[l1][l2]
    
    if str1[l1-1] == str2[l2-1]:
        dp[l1][l2] = 1 + memoizedlongestcommonsubsequencefinal(str1,str2,l1-1,l2-1,dp)
        return dp[l1][l2]
    
    else:
        dp[l1][l2] = max(memoizedlongestcommonsubsequencefinal(str1,str2,l1-1,l2,dp),memoizedlongestcommonsubsequencefinal(str1,str2,l1,l2-1,dp))
        return dp[l1][l2]



def memoizedlongestcommonsubsequence(str1,str2):
    dp= [[-1] * (len(str2)+1) for i in range(len(str1)+1)]
    return memoizedlongestcommonsubsequencefinal(str1,str2,len(str1),len(str2),dp)

print(memoizedlongestcommonsubsequence("ab","ab"))
print(memoizedlongestcommonsubsequence("abcdgh","abedfhr"))


'''
TopDown
'''

def topdownlongestcommonsubsequence(str1,str2):
    dp = [[0] * (len(str2)+1) for i in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    print(dp)
    return dp[i][j]

print(topdownlongestcommonsubsequence("ab","ab"))
#print(topdownlongestcommonsubsequence("abcdgh","abedfhr"))