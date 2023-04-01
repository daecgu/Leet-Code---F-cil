def nextGreaterElement(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    lista = []
    def funcion (numero, lista):
        a = lista.index(numero)
        i = len(lista) -1
        while a < i:
            a += 1
            if numero < lista[a]:
                return lista[a]

        return -1

    for each in nums1:
        lista.append(funcion(each,nums2))

    return lista