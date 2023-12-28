def longestcommonsubsequence(str1,str2):
    dp = [[0] * (len(str2)+1) for i in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    #print(dp)
    strfinal = ""

    while i>0 and j>0:
        if str1[i-1]==str2[j-1]:
            strfinal = str1[i-1] + strfinal 
            i-=1
            j-=1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i-=1
            else: #dp[i-1][j] < dp[i][j-1]:
                j-=1





    return strfinal

print(longestcommonsubsequence("abczyzabcd","abcd"))
print(longestcommonsubsequence("gabcdgh","abcdfhr"))
print(longestcommonsubsequence("zxabcdezy","yzabcdezx"))


