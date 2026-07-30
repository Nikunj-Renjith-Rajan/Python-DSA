# Write code for checking whether a string is a subsequence of another string

def checkSubSeq(str1,str2):
    i=0
    j=0
    while i<len(str1) and j<len(str2):
        if str1[i]==str2[j]:
            i+=1
            j+=1
        else:
            i+=1
    if j==len(str2):
        return True
    else:
        return False
    
str1="Watashi na nowa Kira Yoshikage"
str2="WnnKg"
print(checkSubSeq(str1,str2))
