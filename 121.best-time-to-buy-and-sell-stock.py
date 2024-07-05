#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#
# Need find the lowest price to buy, and the highest price to sell
# Find the maximum profit you can achieve from one transaction (buy once and sell once).
# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min_price = float('inf') 
        max_profit = 0 

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
        

    """
        price = 7: min_price is updated to 7. No change in max_profit 
        price = 1: min_price is updated to 1 (since 1 < 7). No change in max_profit (since 1 - 1 = 0 which is not greater than 0).
        price = 5: max_profit is updated to 4 (since 5 - 1 = 4 which is greater than 0).
        price = 3: No change in min_price or max_profit (since 3 - 1 = 2 which is not greater than 4).
        price = 6: max_profit is updated to 5 (since 6 - 1 = 5 which is greater than 4).
        price = 4: No change in min_price or max_profit (since 4 - 1 = 3 which is not greater than 5).
    """
    """
    Other solution
    prices = [7, 1, 5, 3, 6, 4]
    ans = 0
    pre = prices[0]

    for i in range(1, len(prices)):
        pre = min(pre, prices[i])  # Update the minimum price so far
        print(pre)  # Print the current minimum price
        ans = max(prices[i] - pre, ans)  # Update the maximum profit
    print(ans)  # Output the maximum profit
    """
# @lc code=end

