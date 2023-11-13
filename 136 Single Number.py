def singleNumber(nums: list[int]) -> int:
    a = 0
    # Se va haciendo el XOR (es un exculsivo acumulativo) en binario.
    """
    Ejemplo:
    1,2,3,4,1,2,3
    se hace el binario y se van sumando:
    1 ^ 10 = 11
    11 ^ 11 = 0
    100 ^ 1 = 101
    101 ^ 10 = 111
    111 ^ 11 = 100 
    Respuesta = 100 = 4
    """
    for i in nums:
        a = a ^ i
    return a

lista = [1,2,3,4,3,2,1]

print(singleNumber(lista))
