def halvesAreAlike(n):
    def sumadelcuadradodenumeros(strdenum): ## esta es la forma ineficiente
        total = 0
        for each in strdenum:
            total = total + int(each) ** 2
        return total

    pasados = [1]
    while n != 1 and n not in pasados:
        pasados.append(n)
        n = sumadelcuadradodenumeros(str(n))


    if n == 1:
        return True
    else:
        return False

"""
# esta es la forma eficiente de realizar el bucle ya que el acceso a memoria es más lento que las operacioens.
    def sumadelcuadradodenumeros(n):  #teniendo en cuenta que ahora es un entero y no un str
        total = 0                     # para el resto del programa   
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
        return total
"""

n=7
print(halvesAreAlike(n))