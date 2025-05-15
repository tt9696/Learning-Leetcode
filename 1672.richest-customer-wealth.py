#
# @lc app=leetcode id=1672 lang=python
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for customer in accounts:
            total = sum(customer)
            if total >= max_wealth:
                max_wealth = total
                # or max_wealth = max(max_wealth, total)
        return max_wealth
# @lc code=end

