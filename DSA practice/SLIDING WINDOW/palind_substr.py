# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
def countSubstrings(s):
        count=0
        def expand(left,right):
            c=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                c+=1
                left-=1
                right+=1
            return c

        for i in range(len(s)):
            count+=expand(i,i)
            count+=expand(i,i+1)

        return count

s="aaabaaa"
print(countSubstrings(s))