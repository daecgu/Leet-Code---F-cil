def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    total = 0
    suma = 0
    for each in accounts:
        for x in each:
            suma += x
        if suma > total:
            total = suma
        suma = 0
    return total