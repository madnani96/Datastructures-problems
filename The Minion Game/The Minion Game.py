def minion_game(string):
    vowel =['A','E','I','O','U']
    Stuart=0
    Kevin=0
    for i in range(len(string)):
        if string[i] in vowel:
            Kevin+= len(string)-i
        else:
            Stuart+=len(string)-i
    if Stuart>Kevin:
        print("Stuart"+" "+"%d" %Stuart)
    elif Kevin>Stuart:
        print("Kevin"+" "+"%d" %Kevin)
    else:
        print("Draw")
   

if __name__ == '__main__':
    s = input()
    minion_game(s)