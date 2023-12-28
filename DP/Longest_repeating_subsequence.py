'''
Longest Repeating Subsequence
Given a string, print the longest repeating subsequence such that the two subsequence 
don’t have same string character at same position, i.e., 
any i’th character in the two subsequences shouldn’t have the same index in the original string.
Example:
Input: str = "aab"
Output: "a"
The two subsequence are 'a'(first) and 'a' 
(second). Note that 'b' cannot be considered 
as part of subsequence as it would be at same
index in both.



We just need to add another condition for i!=j
'''


'''
TopDown
'''

def topdownlongestcommonsubsequence(str1,str2):
    dp = [[0] * (len(str2)+1) for i in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1] and i!=j:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    print(dp)
    return dp[i][j]

print(topdownlongestcommonsubsequence("aabebcdd","aabebcdd"))