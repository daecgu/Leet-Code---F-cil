def mergeAlternately(word1,word2):
    """re = '' #respuesta más eficiente hay que importar: from itertools import zip_longest
    for e in zip_longest(word1, word2, fillvalue=''):
        re += ''.join(e)
    return re"""
    i=0
    resultado=""
    if len(word1)<len(word2):
        while i<len(word1):
            resultado= resultado + word1[i] + word2[i]
            i += 1
        while i<len(word2):
            resultado = resultado + word2[i]
            i += 1
    else:
        while i<len(word2):
            resultado= resultado + word1[i] + word2[i]
            i += 1
        while i<len(word1):
            resultado = resultado + word1[i]
            i += 1
    return resultado
s="abc"
t="def"
print(mergeAlternately(s,t))