def checkStraightLine(coordinates):
    """
    :type coordinates: List[List[int]]
    :rtype: bool
    """
    # linea recta: Y = mX +b
    # m = (y2 -y1) / (x2 -x1)
    # b = y1 - m*x1
    def es_linea(m,b,y,x):
        if 0 == (m*x+b-y):
            return True
        else:
            return False

    x1 = coordinates[0][0]
    x2 = coordinates[1][0]
    y1 = coordinates[0][1]
    y2 = coordinates[1][1]
    i = len(coordinates) - 1
    j = 1
    while x1 == x2 and y1 == y2 and j<i:
        y2 = coordinates[j][0]
        x2 = coordinates[j][0]
        if j == i and x1 == x2 and y1 == y2:
            return False
        j += 1

    if (y2-y1) != 0 and (x2-x1) != 0:
        m = (y2-y1) / (x2 - x1)
        b = y1 - m * x1
        for each in coordinates:
            if not es_linea(m, b, each[1], each[0]):
                return False
    elif (x2-x1) == 0:
        for each in coordinates:
            if each[0] != x1:
                return False
    else:
        for each in coordinates:
            if each[1] != y1:
                return False

    return True


print(checkStraightLine([[2,1],[4,2],[6,3]]))

""" while x1 == x2 and y1 == y2 and j<i:
        y2 = coordinates[j][0]
        x2 = coordinates[j][0]
        if j == i and x1 == x2 and y1 == y2:
            return False
        j += 1
    m = (y2-y1) / (x2 - x1)
    b = y1 - m * x1

    for each in coordinates:
        if not es_linea(m,b,each[1],each[0]):
            return False"""