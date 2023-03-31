def maximumWealth(accounts):
    richest = 0
    for each in accounts:
        richest=max(richest,sum(each)) #esta opción es más eficiente y más legible.
        """a = sum(each)
        if a > richest:
            richest = a"""

    return richest
accounts= [[1,5],[7,3],[3,5]]
print(maximumWealth(accounts))