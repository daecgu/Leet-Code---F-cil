def diagonalSum(mat):
    i = 0
    j = len(mat[0]) - 1
    f = j + 1
    suma = 0
    while i < f:
        suma += mat[i][i]
        if j != i:
            suma += mat[i][j]
        i += 1
        j -= 1
    return suma
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))