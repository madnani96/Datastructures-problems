'''
Minimum number of deletions and insertions to transform one string into another
Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.
Example:
Input : str1 = "geeksforgeeks", str2 = "geeks"
Output : Minimum Deletion = 8
         Minimum Insertion = 0 

Deletion will be len(str1)-LCS_length
Insertion will be lens(str2)-LCS_length
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

def calculateinsertiondeletion(str1,str2):
    lcs =  topdownlongestcommonsubsequence(str1,str2)
    return len(str1)-lcs, len(str2)-lcs

str1 = "geeksforgeeks"
str2 = "geeks"
deletion,insertion = calculateinsertiondeletion(str1,str2)
print("Insertion",insertion)
print("Deletion",deletion)