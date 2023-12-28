def shortestcommonsupersequence(str1,str2):
    dp = [[0] * (len(str2)+1) for i in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    

    
    return  len(str1)+len(str2)-dp[i][j]

print(shortestcommonsupersequence("abczyzabcd","abcd"))
print(shortestcommonsupersequence("gabcdgh","abcdfhr"))
print(shortestcommonsupersequence("zxabcdezy","yzabcdezx"))

print(shortestcommonsupersequence("eke","geek"))