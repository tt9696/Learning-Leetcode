#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
# You are allowed to complete as many transactions as you like (buy and sell multiple times).
# You can only hold one share of the stock at a time (you must sell before you buy again).

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i]-prices[i-1]
        return total_profit
    
    """
    Day 1 (i = 1):
    prices[1] = 1, prices[0] = 7
    prices[1] <= prices[0], so no profit is added.
    
    Day 2 (i = 2):
    prices[2] = 5, prices[1] = 1
    prices[2] > prices[1], so add 5 - 1 = 4 to ans.
    ans = 4
    
    Day 3 (i = 3):
    prices[3] = 3, prices[2] = 5
    prices[3] <= prices[2], so no profit is added.
    
    Day 4 (i = 4):
    prices[4] = 6, prices[3] = 3
    prices[4] > prices[3], so add 6 - 3 = 3 to ans.
    ans = 4 + 3 = 7

    Day 5 (i = 5):
    prices[5] = 4, prices[4] = 6
    prices[5] <= prices[4], so no profit is added.
    Finally, the total profit (ans) is 7.
    
    """
# @lc code=end

