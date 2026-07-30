# You are given two integer arrays of different lengths that are already sorted in ascending order. 
# Write a function to compute their exact intersection—meaning the elements that appear in both arrays. 
# If a number appears multiple times in both arrays, it should appear that many times in your result.

def arrIntersection(arr1,arr2):
    i,j=0,0
    res=[]
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]>arr2[j]:
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            res.append(arr1[i])
            i+=1
            j+=1
    return res

a=[1,2,2,3,5,6,7,7,8,13]
b=[3,3,4,5,5,6,7,7,10,11,14]
print(arrIntersection(a,b))