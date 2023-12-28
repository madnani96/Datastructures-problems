def isPalindrome(s: str):
        s= s.lower().strip()
        i=0
        j=len(s)-1
        while(i<j):
            while(i<len(s) and s[i].isalpha()== False and s[i].isnumeric() == False):
                i+=1
            while(j>0 and s[j].isalpha()== False and s[j].isnumeric() == False):
                j-=1
            if(i<len(s) and j>0):
                if s[i] != s[j]:
                    return False
            i+=1
            j-=1
        
        return True

print(isPalindrome("0P"))

