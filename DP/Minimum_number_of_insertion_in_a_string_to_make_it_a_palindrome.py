'''
Minimum number of insertions to make a string palindrome
Given a string, find the minimum number of characters to be
inserted to form Palindrome string out of given string

Examples:
ab: Number of insertions required is 1. bab
aa: Number of insertions required is 0. aa
'''
#implemnet longest palindromix sequence: then length of string - longest palindromix sequence length is ans

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
str2 = "babbb" 
str2=str1[::-1]
print(len(str1)-topdownlongestcommonsubsequence(str1,str2))