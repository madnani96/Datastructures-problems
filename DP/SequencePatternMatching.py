'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
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
def checkif_a_is_subsequence_of_b(a,b):
    subsequence = topdownlongestcommonsubsequence(a,b)
    
    if subsequence == len(a):
        return True
    else:
        return False 
s="abc"
t="ahbgdc"
s = "axc"
t = "ahbgdc"

print(checkif_a_is_subsequence_of_b(s,t))
#print(topdownlongestcommonsubsequence("aabebcdd","aabebcdd"))