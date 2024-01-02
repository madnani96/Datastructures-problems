#https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
#https://www.youtube.com/watch?v=pGVguAcWX4g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=38

'''recursive'''

def countnumberofways(s,i,j,isTrue):

    if i>j:
        return False
    
    if i==j:
        if isTrue == True:
            return s[i] == 'T'
        else:
            return s[i] == 'F'


    ans = 0
    for k in range(i+1,j,2):
        rt= countnumberofways(s,k+1,j,True)
        rf= countnumberofways(s,k+1,j,False)
        lt= countnumberofways(s,i,k-1,True)
        lf= countnumberofways(s,i,k-1,False)


        if s[k] == '^':
            if isTrue == True:
                ans += (rt * lf + rf * lt)
            else:
                ans+= (rf * lf + rt * lt)
        elif s[k] == '&':
            if isTrue == True:
                ans+= rt * lt
            else:
                ans+= (rf * lf + rt * lf + rf * lt)
        elif s[k] == '|':
            if isTrue == True:
                ans += (rt * lt + rf * lt + rt * lf)
            else:
                ans += rf * lf 
    return ans


S = ['T', '|', 'F', '&', 'T', '^', 'T']
S = ['T', '^', 'F', '&', 'T']


count = countnumberofways(S, 0, len(S) - 1, True)
print(count)



'''memoized map version'''

def memoizedcountnumberofways(s,i,j,isTrue):
    key = str(i) + '_' + str(j) + '_' + str(isTrue)
    if i>j:
        return False
    
    if i==j:
        if isTrue == True:
            return s[i] == 'T'
        else:
            return s[i] == 'F'
        
    if key in dict:
        return dict[key]

    ans = 0
    for k in range(i+1,j,2):
        rt= memoizedcountnumberofways(s,k+1,j,True)
        rf= memoizedcountnumberofways(s,k+1,j,False)
        lt= memoizedcountnumberofways(s,i,k-1,True)
        lf= memoizedcountnumberofways(s,i,k-1,False)


        if s[k] == '^':
            if isTrue == True:
                ans += (rt * lf + rf * lt)
            else:
                ans+= (rf * lf + rt * lt)
        elif s[k] == '&':
            if isTrue == True:
                ans+= rt * lt
            else:
                ans+= (rf * lf + rt * lf + rf * lt)
        elif s[k] == '|':
            if isTrue == True:
                ans += (rt * lt + rf * lt + rt * lf)
            else:
                ans += rf * lf 
    dict[key] = ans
    return ans


S = 'T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F'
#S = ['T', '^', 'F', '&', 'T']


dict={}
print(memoizedcountnumberofways(S, 0, len(S) - 1, 1))
#print(dict)


'''memoized 3d matrix version'''


def memoized3dcountnumberofways(s,i,j,isTrue):

    if i>j:
        return False
    
    if i==j:
        if isTrue == True:
            return int(s[i] == 'T')
        else:
            return int(s[i] == 'F')
    if dp[i][j][int(isTrue)]!= -1:
        return dp[i][j][int(isTrue)]

    ans = 0
    for k in range(i+1,j,2):
        rt= memoized3dcountnumberofways(s,k+1,j,True)
        rf= memoized3dcountnumberofways(s,k+1,j,False)
        lt= memoized3dcountnumberofways(s,i,k-1,True)
        lf= memoized3dcountnumberofways(s,i,k-1,False)


        if s[k] == '^':
            if isTrue == True:
                ans += (rt * lf + rf * lt)
            else:
                ans+= (rf * lf + rt * lt)
        elif s[k] == '&':
            if isTrue == True:
                ans+= rt * lt
            else:
                ans+= (rf * lf + rt * lf + rf * lt)
        elif s[k] == '|':
            if isTrue == True:
                ans += (rt * lt + rf * lt + rt * lf)
            else:
                ans += rf * lf 
    dp[i][j][int(isTrue)] = ans
    return ans


S = ['T', '|', 'F', '&', 'T', '^', 'T']
S= 'T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F'
#S = ['T', '^', 'F', '&', 'T']
import numpy as np



# Create a 3D matrix filled with -1
dp = np.full((len(S), len(S), 2), -1, dtype=int)

print(memoized3dcountnumberofways(S, 0, len(S) - 1, 1))



