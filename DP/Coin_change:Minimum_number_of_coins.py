'''
Coin Change Problem Minimum Numbers of coins
Given a value V, if we want to make change for V cents, 
and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, 
what is the minimum number of coins to make the change?
Example:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 
'''

temp=[]
def coinchange(coinarr,Nleft,n,count):
    
    if n==0 and Nleft!=0:
        return 99999999
    
    if Nleft==0:
        return count      
    
    if coinarr[n-1]<=Nleft:
        return min(coinchange(coinarr,Nleft-coinarr[n-1],n,count+1),coinchange(coinarr, Nleft,n-1,count))
    else:
        return coinchange(coinarr, Nleft,n-1,count)
    
print(coinchange([25,10,5],30,3,0))
print(coinchange([2,5,10,1],27,4,0))
print(coinchange([186,419,83,408],6249,4,0))

'''
memoized
'''

def memoizedcoinchange(coinarr,Nleft):
    dp = [[-1]*(Nleft+1) for i in range(len(coinarr)+1)]
    
    return memoizedcoinchangefinal(coinarr, len(coinarr),Nleft, dp,0)

def memoizedcoinchangefinal(coinarr,n,Nleft,dp,count):
    if Nleft == 0:
        return count
    
    if n == 0 and Nleft != 0:
        return 9999999
    
    
    
    
    if dp[n][Nleft] != -1:
        return dp[n][Nleft]

    
    if coinarr[n-1] <=Nleft:
         
        dp[n][Nleft]=min(memoizedcoinchangefinal(coinarr,n,Nleft-coinarr[n-1],dp,count+1) ,memoizedcoinchangefinal(coinarr, n-1,Nleft,dp,count))
        return dp[n][Nleft]
    
    else:
        dp[n][Nleft] = memoizedcoinchangefinal(coinarr,n-1, Nleft,dp,count)
        return dp[n][Nleft]

print(memoizedcoinchange([25,10,5],30))
print(memoizedcoinchange([2,5,10,1],27))




'''
above memoized not working for some reason
'''
def memoizedcoinchange(coinarr, Nleft):
    dp = [[-1] * (Nleft + 1) for _ in range(len(coinarr) + 1)]
    return memoizedcoinchangefinal(coinarr, len(coinarr), Nleft, dp)


def memoizedcoinchangefinal(coinarr, n, Nleft, dp):
    if Nleft == 0:
        return 0
    if n == 0 and Nleft != 0:
        return float('inf')

    if dp[n][Nleft] != -1:
        return dp[n][Nleft]

    if coinarr[n - 1] <= Nleft:
        dp[n][Nleft] = min(memoizedcoinchangefinal(coinarr, n, Nleft - coinarr[n - 1], dp) + 1,
                           memoizedcoinchangefinal(coinarr, n - 1, Nleft, dp))
    else:
        dp[n][Nleft] = memoizedcoinchangefinal(coinarr, n - 1, Nleft, dp)

    return dp[n][Nleft]


print(memoizedcoinchange([25, 10, 5], 30))
print(memoizedcoinchange([2, 5, 10, 1], 27))
