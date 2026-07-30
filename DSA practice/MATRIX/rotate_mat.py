# ROTATE THE MATRIX 90 DEGREES CLOCKWISE
r=3
c=3
mat=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=" ")
    print()
print()
for i in range(r):
    for j in range(i+1,c):
        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
for i in range(r):
    mat[i].reverse()
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=" ")
    print()

#ROTATE THE MATRIX 270 DEGREES
r=3
c=3
mat=[[1,2,3],[4,5,6],[7,8,9]]
print()
for i in range(r):
    for j in range(i+1,c):
        mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
mat.reverse()
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=" ")
    print()

