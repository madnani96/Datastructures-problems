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






