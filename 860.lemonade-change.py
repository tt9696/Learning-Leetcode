#
# @lc app=leetcode id=860 lang=python
#
# [860] Lemonade Change
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10: #give 5 change
                if five == 0: # no have 5
                    return False 
                five -= 1 # give 5 change
                ten += 1
            else: #20, need give change 10 and 5
                if ten > 0 and five > 0:
                    ten -= 1 
                    five -=1 
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
# @lc code=end

