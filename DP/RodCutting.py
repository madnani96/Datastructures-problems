'''
Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
{0,1,2,3,4,5,6,7}
Output:
22
Explanation:
The maximum obtainable value is 22 by 
cutting in two pieces of lengths 2 and 
6, i.e., 5+17=22.
'''
import numpy as np
def rodcuting(pricearr,rodlengthleft,length):
    
    
    if length==0:
        return 0      
    
    if rodlengthleft>=length:
        return max(pricearr[length-1]+rodcuting(pricearr,rodlengthleft-length,length),rodcuting(pricearr,rodlengthleft,length-1))
    else:
        return rodcuting(pricearr,rodlengthleft,length-1)

A = [ 1, 5, 8, 9, 10, 17, 17, 20 ]
n = len(A)
total_len = len(A)
print(rodcuting(A, len(A), len(A)))
'''
memoized version

'''

def memoizedrodcutting(pricearr, n, rodlengthleft, dp):
    if n==0:
        return 0
    
    if dp[n][rodlengthleft]!=-1:
        return dp[n][rodlengthleft]
    
    if n<=rodlengthleft:
        dp[n][rodlengthleft] = max(pricearr[n-1]+memoizedrodcutting(pricearr,n,rodlengthleft-n,dp),memoizedrodcutting(pricearr,n-1,rodlengthleft,dp))
        return dp[n][rodlengthleft]
    else:
        dp[n][rodlengthleft] = memoizedrodcutting(pricearr,n-1,rodlengthleft,dp)
        return dp[n][rodlengthleft]


def memoizedrodcuttingfinal(pricearr,rodlengthleft):
    #dp = np.zeros((rodlengthleft+1,rodlengthleft+1))
    dp=[[0]*(rodlengthleft+1) for i in range(rodlengthleft+1)]
    for x in range(rodlengthleft+1):
        for y in range(rodlengthleft+1):
            dp[x][y]=-1
    '''
    for x in range(rodlengthleft+1):
        dp[0][x]=0
    for y in range(rodlengthleft+1):
        dp[y][0]=
    '''
    return memoizedrodcutting(pricearr,rodlengthleft,rodlengthleft,dp)

print(memoizedrodcuttingfinal(A, len(A)))



'''
top down approach
'''

def topdownrodcutting(pricearr, rodlengthleft):

    dp=[[0]*(rodlengthleft+1) for i in range(rodlengthleft+1)]

    for i in range(1,len(pricearr)+1):
        for j in range(1,rodlengthleft+1):
            if i<=j:
                dp[i][j] = max( pricearr[i-1] +dp[i][j-i] ,    dp[i-1][j])
            else:
                dp[i][j]= dp[i-1][j]



    return dp[i][j]


print(topdownrodcutting(A,len(A)))






