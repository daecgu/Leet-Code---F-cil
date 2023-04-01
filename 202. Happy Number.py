def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    def sumadelcuadradodenumeros(n):
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        """for each in n:
            total = total + int(each)**2"""
        return total

    pasados = set()
    while n != 1 and n not in pasados:
        pasados.add(n)
        n = sumadelcuadradodenumeros(n)

    if n == 1:
        return True
    else:
        return False