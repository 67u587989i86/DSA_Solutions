def maxProfit(prices):
    min_price = float('inf')   # lowest price seen so far , plus infinity , minus = float('-inf')
    max_profit = 0            # best profit seen so far

    for currentprice in prices:
        # keep track of the cheapest day up to now
        min_price = min(min_price, currentprice)
        # what if we sold today?
        max_profit = max(max_profit, currentprice - min_price)

    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))  # ➜ 5
print(maxProfit([3, 6, 1, 2]))        # ➜ 3
print(maxProfit([2, 1, 2, 1, 0, 1]))  # ➜ 1
