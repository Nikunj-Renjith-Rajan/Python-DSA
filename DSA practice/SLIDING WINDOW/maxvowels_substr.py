# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

def maxVowels(s, k):
    v="aeiou"
    c=0
    if k==1:
        if s[0] in v:
            return 1
    for i in range(k):
        if s[i] in v:
            c+=1
    maxc=c
    for i in range(k,len(s)):
        if s[i-k] in v:
            c-=1
        if s[i] in v:
            c+=1
        maxc=max(maxc,c)
    return maxc

s="abciiidef"
k=3
print(maxVowels(s,k))
        