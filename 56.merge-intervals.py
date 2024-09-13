#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
# https://www.youtube.com/watch?v=44H3cEC2fFM

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i: i[0]) # intervals = [[1,3], [2,6], [8,10], [15,18]]
        output = [intervals[0]]  # output = [[1, 3]]
        # second => output = [[1, 6]]

        for start, end in intervals[1:]: # intervals[1:] => [[2,6],[8,10],[15,18]]
            lastEnd = output[-1][1] # lastEnd is initially 3, the end time of the first interval [1, 3]
            if start <= lastEnd: # 2 < 3
                output[-1][1] = max(lastEnd, end) # output[-1][1] = max(3, 6), output = [[1, 6]]
            else: 
                output.append([start, end])
        return output
    
# @lc code=end

