# Find maximum row sum and its index
def maxrowsum(mat):
    maxsum=0
    maxindex=-1
    r=len(mat)
    c=len(mat[0])
    for i in range(r):
        crs=0
        for j in range(c):
            crs+=mat[i][j]
        if crs>maxsum:
            maxsum=crs
            maxindex=i
    return maxsum,maxindex

# Find maximum column sum and its index
def maxcolsum(mat):
    maxsum=0
    maxindex=-1
    r=len(mat)
    c=len(mat[0])
    for i in range(c):
        crs=0
        for j in range(r):
            crs+=mat[j][i]
        if crs>maxsum:
            maxsum=crs
            maxindex=i
    return maxsum,maxindex

mat=[[1,2,3,1],[4,3,2,1],[1,2,4,5],[4,3,2,6],[1,2,7,4]]
print(*maxrowsum(mat))
print(*maxcolsum(mat))