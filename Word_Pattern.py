def wordPattern(pattern: str, s: str): 
        temp = s.split(" ")
        
        if len(temp) != len(pattern):
            return False
        
        dict = {}
        
        for x in range(len(pattern)):
            if pattern[x] not in dict.keys():
                dict[pattern[x]]=temp[x]
        
        for x in range(len(pattern)):
            if dict[pattern[x]] != temp[x]:
                return False
        
        dummy1 = len(set(dict.values()))
        dummy2 = len(dict.values())
        if dummy1 != dummy2:
            return False

        return True