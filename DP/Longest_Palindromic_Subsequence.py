'''
Longest Palindromic Subsequence
Given a sequence, find the length of the longest palindromic subsequence in it.
Example :
Input:"bbbab"
Output:4

its an lcs problem just reverse the string provided and put in lcs function

'''


def topdownlongestcommonsubsequence(str1,str2):
    dp = [[0] * (len(str2)+1) for i in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    return dp[i][j]
str1 = "bbbab"
str2=str1[::-1]
print(topdownlongestcommonsubsequence(str1,str2))