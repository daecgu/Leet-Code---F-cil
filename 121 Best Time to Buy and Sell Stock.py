def maxProfit(prices: list[int]) -> int:
    low_price: int = prices[0]
    max_profit: int = 0
    for each in prices:
        if each < low_price:
            low_price = each
        elif (each - low_price) > max_profit:
            max_profit = each - low_price
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
