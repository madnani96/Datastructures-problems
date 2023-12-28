#variation of lcs


def topdownlongestcommonsubsequence(str1,str2):
    dp = [[0] * (len(str2)+1) for i in range(len(str1)+1)]
    bc=0
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                
                dp[i][j] = 1 + dp[i-1][j-1]
                bc= max(bc,1 + dp[i-1][j-1])

            
    
    return bc
print(topdownlongestcommonsubsequence("abc","abc"))
print(topdownlongestcommonsubsequence("abclgh","abcdfhr"))

