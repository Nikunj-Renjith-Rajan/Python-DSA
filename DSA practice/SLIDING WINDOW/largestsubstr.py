# You are given a string, and your goal is to find the length of the 
# longest contiguous substring that contains no duplicate characters.
def largestSubString(s):
    if len(s)==0:
        return 0
    maxlen=0
    l=0
    r=0
    dic={}
    while(r<len(s)):
        if s[r] not in dic:
            dic[s[r]]=r
        else:
            if l<=dic[s[r]]:
                l=dic[s[r]]+1
            dic[s[r]]=r
        maxlen=max(maxlen,r-l+1)
        r+=1
    return maxlen

s="abbababcddbegjkdb"
print(largestSubString(s))
