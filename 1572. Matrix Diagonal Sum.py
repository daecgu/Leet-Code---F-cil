def diagonalSum(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    l = len(mat) - 1
    y = 0
    total = 0
    x= l
    while y <= l:
        total += mat[y][y]
        total += mat[x][y]
        y += 1
        x -= 1

    if l%2 == 1:
        return total
    else:
        total -= mat[l//2][l//2]
