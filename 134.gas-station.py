#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1
        
        remain_tank = 0 # gas[i] - cost[i]
        total_tank = 0
        start = 0 # need return where to start

        for i in range(len(gas)):# 0 1 2 3 4
            remain_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            if remain_tank < 0:
                start = i + 1 # move to next station
                remain_tank = 0

        return start if total_tank>=0 else -1
# @lc code=end

