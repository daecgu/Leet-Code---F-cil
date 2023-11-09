def ispalindrome(s: str) -> bool:
    # Más Corta en líneas de código
    # s = ''.join(filter(str.isalnum, s)).lower()
    # return s == s[::-1]

    # Más eficiente en memoria, buen rendimiento.
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

    # Menos eficiente
    # x = ""
    # y = ""
    # for letra in s[::-1]:
    #     if letra.isalnum():
    #         x = x + letra.lower()
    #         y = letra.lower() + y
    # if x == y:
    #     return True
    # return False



print(ispalindrome("A man, a plan, a canal: Panama"))
