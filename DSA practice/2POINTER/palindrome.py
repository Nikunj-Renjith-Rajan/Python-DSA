# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
# removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric 
# characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

#METHOD 1 : BRUTE FORCE
def isPalindrome1(s):
        s1=[]
        for i in s.lower():
            if i.isalnum():
                s1.append(i)
        return s1==s1[::-1]

#METHOD 2 : 2 POINTER
def isPalindrome2(s):
        i= 0 
        j=len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

s="A man, a plan, a canal: Panama"
print(isPalindrome1(s))
print(isPalindrome2(s))