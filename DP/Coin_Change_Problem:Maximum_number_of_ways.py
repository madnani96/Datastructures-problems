'''
Given a value N, if we want to make change for N cents, and we have infinite supply 
of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?
The order of coins doesn’t matter.
Example:
for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
https://leetcode.com/problems/coin-change-ii/
'''



'''
recursive
'''


def coinchange(coinarr,Nleft,n):
    
    
    if n==0 and Nleft!=0:
        return 0
    if Nleft==0:
        return 1      
    
    if coinarr[n-1]<=Nleft:
        return coinchange(coinarr,Nleft-coinarr[n-1],n) + coinchange(coinarr, Nleft,n-1)
    
    else:
        return coinchange(coinarr, Nleft,n-1)


coinarr=[1,2,3]
n=4
print(coinchange(coinarr,4,3))


'''
memoized
'''

def memoizedcoinchange(coinarr,Nleft):
    dp = [[-1]*(Nleft+1) for i in range(len(coinarr)+1)]
    
    return memoizedcoinchangefinal(coinarr, len(coinarr),Nleft, dp)

def memoizedcoinchangefinal(coinarr,n,Nleft,dp):
    
    if Nleft == 0:
        return 1
    
    if n == 0 and Nleft != 0:
        return 0
    
    
    
    if dp[n][Nleft] != -1:
        return dp[n][Nleft]

    
    if coinarr[n-1] <=Nleft:
         
        dp[n][Nleft]=memoizedcoinchangefinal(coinarr,n,Nleft-coinarr[n-1],dp) + memoizedcoinchangefinal(coinarr, n-1,Nleft,dp)
        return dp[n][Nleft]
    
    else:
        dp[n][Nleft] = memoizedcoinchangefinal(coinarr,n-1, Nleft,dp)
        return dp[n][Nleft]

print(memoizedcoinchange(coinarr,n))



'''
above sol better than 99% of submitted soln
for top down
initialization as follows
0000000
1
1
1
1
'''