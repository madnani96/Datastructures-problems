'''
def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        print(lst)
        stri="/"
        stck=[]
        for x in lst:
            if x == '' or x == '.':
                continue
            elif  x == '..':
                if len(stck)!=0:
                    stck.pop()
            else:
                stck.append(x)
        
        for x in stck:
            stri =  stri + str(x) + "/"

        if len(stri)!=1:
            stri=stri[:len(stri)-1]
        return stri


'''
