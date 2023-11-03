# esta es la forma que se me ha ocurrido
def get_row(row_index) -> list[int]:
    ans = [1]
    if row_index == 0:
        return ans
    i = 1
    while i < row_index:
        j = len(ans)
        while j > 0:
            try:
                ans[j] = ans[j] + ans[j-1]
            except:
                ans.append(1)
                ans[j] = 1 + ans[j-1]
            finally:
                j -= 1
        i += 1
    ans.append(1)

    return ans

print(get_row(6))


## esta es la forma matemática de calcular cada una de las posiciones
def get_row_optimized(rowIndex):
    res = [1]
    prev = 1
    for k in range (1, rowIndex +1):
        next_val= prev * (rowIndex -k +1) // k
        res.append(next_val)
        prev = next_val
    return res

print(get_row_optimized(6))