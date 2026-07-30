def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    mapst = {}
    mapts = {}
    for i in range(len(s)):
        a = s[i]
        b = t[i]
        if a in mapst:
            if mapst[a] != b:
                return False
        else:
            mapst[a] = b
        if b in mapts:
            if mapts[b] != a:
                return False
        else:
            mapts[b] = a
    return True

s="egg"
t="add"
print(isIsomorphic(s,t))

    
                
        