def createnewnum(n):
    n1= str(n)
    sum=0
    for x in n1:
        sum+=int(x) * int(x)

    
    return sum
print(createnewnum(100))


def isHappy(n):
    dict={}
    while (n != 1):
        n = createnewnum(n)

        if n in dict.keys():
            return False 
        dict[n] =1
    return True

print(isHappy(19))
print(isHappy(2))


