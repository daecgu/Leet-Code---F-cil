from collections import Counter
def findTheDifference(s, t):
    cs = Counter(s)
    ct = Counter(t)
    ct.subtract(cs)
    cs= list(+ct)
    return cs[0]
    #print(str(sorted(ct.elements())))

""" 
otra opción cuando solo son letras minúsculas:
tähed = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(tähed)):
            if s.count(tähed[i]) != t.count(tähed[i]):
                return tähed[i]
                
"""

s="hola"
t="holaa"
print(findTheDifference(s,t))