def matrixchainmultrecursive(arr, i, j, minimum):
    if i>=j:
        return 0
    for k in range(i,j):
        minimum = min(matrixchainmultrecursive(arr,i,k,minimum) + matrixchainmultrecursive(arr,k+1,j,minimum) + arr[i-1]*arr[k]*arr[j], minimum)

    return minimum 

print(matrixchainmultrecursive([40,20,30,10,30],1,4,9999999))


def memoizedmatrixchainmultrecursive(arr, i, j, minimum,dp):
    if i>=j:
        return 0
    
    if dp[i][j]!=-1:
        return dp[i][j]
    for k in range(i,j):
        minimum = min(memoizedmatrixchainmultrecursive(arr,i,k,minimum,dp) + memoizedmatrixchainmultrecursive(arr,k+1,j,minimum,dp) + arr[i-1]*arr[k]*arr[j], minimum)
    dp[i][j] = minimum
    return  dp[i][j]



def memoizedmatrixchainmultrecursivefinal(arr,i,j,dp):
    dp = [[-1]*(len(arr)+1) for k in range(len(arr)+1)]
    return memoizedmatrixchainmultrecursive(arr, i, j, 9999999,dp)


print(memoizedmatrixchainmultrecursivefinal([40,20,30,10,30],1,4,9999999))