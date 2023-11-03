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
