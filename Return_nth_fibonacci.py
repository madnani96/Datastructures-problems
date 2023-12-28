#Fib sequence 1,1,2,3,5,8,13,21,34,55

def fibonacci(n):
    if n == 1 or n == 2: 
        return 1
    else:
    
    
        count = 2
        prevprevnum = 1
        prevnum = 1
        
        while count != n:
            temp=prevnum
            prevnum = prevnum+prevprevnum
            prevprevnum=temp

            
            count+=1
        return prevnum

print(fibonacci(30))


def recursivefibonacci(n):
    if n == 1 or n == 2: 

        result = 1
    else:
        result = recursivefibonacci(n-1)+recursivefibonacci(n-2)
        

    return result

        

print(recursivefibonacci(30))





# A memoized solution
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)


# A bottom-up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]