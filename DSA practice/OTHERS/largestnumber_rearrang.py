#Given an array of non-negative integers, write a code to arrange them to yield the largest number
arr=[7000,700,70,7,8]
strarr=list(map(str,arr))
for i in range(len(strarr)):
    for j in range(i+1,len(strarr)):
        if strarr[i]+strarr[j]<strarr[j]+strarr[i]:
            strarr[i],strarr[j]=strarr[j],strarr[i]
print("".join(strarr))

#Similarly yield the smallest number 
for i in range(len(strarr)):
    for j in range(i+1,len(strarr)):
        if strarr[i]+strarr[j]>strarr[j]+strarr[i]:
            strarr[i],strarr[j]=strarr[j],strarr[i]
print("".join(strarr))
