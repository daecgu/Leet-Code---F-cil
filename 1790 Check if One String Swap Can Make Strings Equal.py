def areAlmostEqual(s1, s2):
    if len(s1) != len(s2):
        return False
    contador = 0
    j = 0
    k = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            contador = contador + 1
            if contador == 1:
                j = i
            else:
                if contador == 2:
                    k = i
                else:
                    return False
    if contador == 0:
        return True
    else:
        if s1[j] == s2[k] and s2[j] == s1[k] and contador == 2:
            return True
        else:
            return False

print(areAlmostEqual("abc","cba"))