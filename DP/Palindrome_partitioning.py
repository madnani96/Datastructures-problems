


def checkpalindrome(s,i,j):
            str=s[i:j+1]
            if str == str[::-1]:
                return True
            else:
                return False

'''
Recursive
'''
def palindromepartitioningrecursive(s,i,j,minimumtemp):
    if i>=j:
        return 0
    if checkpalindrome(s,i,j):
        return 0

    for k in range(i,j):
        minimumtemp = min(1+palindromepartitioningrecursive(s,i,k,minimumtemp)+palindromepartitioningrecursive(s,k+1,j,minimumtemp), minimumtemp)

    return minimumtemp

print(palindromepartitioningrecursive("abcbaa",0,5,9999))


'''
Memoized
'''
def palindromepartitioningmemoized(s,i,j,minimumtemp,dp):
    if i>=j:
        return 0
    if checkpalindrome(s,i,j):
        return 0
    
    if dp[i][j]!=-1:
         return dp[i][j]

    for k in range(i,j):
        minimumtemp = min(1+palindromepartitioningmemoized(s,i,k,minimumtemp,dp)+palindromepartitioningmemoized(s,k+1,j,minimumtemp,dp), minimumtemp)
    
    dp[i][j] = minimumtemp
    return dp[i][j]

def palindromepartitioningmemoizedfinal(s):
     dp =[[-1]*(len(s)+1) for i in range(len(s)+1)]
     return palindromepartitioningmemoized(s, 0,len(s)-1,99999,dp)

print(palindromepartitioningmemoizedfinal("abcbaa"))


'''
Optimized memoization
'''


def optimizedpalindromepartitioningmemoized(s,i,j,minimumtemp,dp,palindromedp):
    if i>=j:
        return 0
    
    if palindromedp[i][j]==-1:
        test = checkpalindrome(s,i,j)
        palindromedp[i][j]=test
        if test:
            return 0
    else:
        if palindromedp[i][j]==True:
            return 0
    
    if dp[i][j]!=-1:
         return dp[i][j]

    for k in range(i,j):
        if dp[i][k]!=-1:
            l = dp[i][k]
        else:
            l = optimizedpalindromepartitioningmemoized(s,i,k,minimumtemp,dp,palindromedp)
        
        if dp[k+1][j]!=-1:
            r = dp[k+1][j]
        else: 
            r = optimizedpalindromepartitioningmemoized(s,k+1,j,minimumtemp,dp,palindromedp)
        minimumtemp = min(1+l+r, minimumtemp)
    
    dp[i][j] = minimumtemp
    return dp[i][j]

def optimizedpalindromepartitioningmemoizedfinal(s):
    dp =[[-1]*(len(s)+1) for i in range(len(s)+1)]
    palindromedp = [[-1]*(len(s)+1) for i in range(len(s)+1)]
    return optimizedpalindromepartitioningmemoized(s, 0,len(s)-1,99999,dp, palindromedp)

print(optimizedpalindromepartitioningmemoizedfinal("abcbaa"))


'''
best approach
'''

def checkpalindrome(s,i,j):
            str=s[i:j+1]
            if str == str[::-1]:
                return True
            else:
                return False
        
def optimizedpalindromepartitioningmemoized(i,j,minimumtemp,dp):
            if i>=j:
                return 0

            if dp[i][j]!=-1:
                return dp[i][j]

            
            if checkpalindrome(s,i,j):
                return 0
    
            for k in range(i,j):

                if checkpalindrome(s,i,k):
                    minimumtemp = min(1+optimizedpalindromepartitioningmemoized(k+1,j,minimumtemp,dp), minimumtemp)
                
            
            dp[i][j] = minimumtemp
            return dp[i][j]
            
s="abcbaa"
dp =[[-1]*(len(s)+1) for i in range(len(s)+1)]
print(optimizedpalindromepartitioningmemoized(0,len(s)-1,99999,dp))
