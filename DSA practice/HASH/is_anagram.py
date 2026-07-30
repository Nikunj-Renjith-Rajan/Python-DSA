#Given two strings s and t, return true if t is an anagram of s, and false otherwise
def isAnagram(s, t):
        if len(s)!=len(t):
            return False
        dic={}
        for char in s:
            if char in dic:
                dic[char]=dic[char] + 1
            else:
                dic[char]=1
        for char in t:
            if char not in dic or dic[char]==0:
                return False
            dic[char]-=1
        return True

print(isAnagram("anagram","nagaram"))