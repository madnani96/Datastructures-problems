def isValid(str):
    stck=[]
    for x in str:
        if stck == []:
            stck.append(x)
        else:
            if(x == '[' or x == '{' or x == '('):
                stck.append(x)
            elif ((stck[-1] == "[" and x == "]") or (stck[-1] == "{" and x == "}") or (stck[-1] == "(" and x == ")")):
                stck.pop()
            else:
                break

    if stck == []:
        return True
        
    else:
        print(stck)
        return False



    




print(isValid("]}}}}"))

