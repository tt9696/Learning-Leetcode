#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
# https://www.youtube.com/watch?v=A8NUOmlwOlM

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(len(intervals)):
              # If newInterval is before the current interval (no overlap), add newInterval and return
            if newInterval[1] < intervals[i][0]: 
                output.append(newInterval)
                return output + intervals[i:] 
            
            # If newInterval is after the current interval (no overlap), add current interval to output
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
                
            else: #  There is overlap, merge the intervals
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1],intervals[i][1])]

        output.append(newInterval)
        # if the case, intervals = [[1, 3], [6, 7], [8, 10]]
        # newInterval = [11, 13], add [11, 13] to the end
        # or

        # intervals = [[1, 3], [6, 7], [8, 10]], newInterval = [5, 9]
        # The loop will merge them into [5, 10], but it won’t add this merged interval to output until the loop finishes
        # need to final append [[1, 3], [5, 10]]
        return output

'''
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
output = [[1,2],[3,10],[12,16]]

if newInterval[1] < intervals[0][0] means it is the first one

(1) elif
intervals[0] = [1,2]
newInterval[1] < intervals[0][0] → 8 < 1 → False
newInterval[0] > intervals[0][1] → 4 > 2 → True
output: [[1,2]]

(2) else
intervals[1] = [3,5]
newInterval[1] < intervals[1][0] → 8 < 3 → False
newInterval[0] > intervals[1][1] → 4 > 5 → False
Else: newInterval = [min(4, 3), max(8, 5)] = [3, 8]. newInterval: [3,8]
...
(3) else
intervals[2] = [6,7]
newInterval = [min(3, 6), max(8, 7)] = [3, 8]. newInterval: [3,8] => unchanged

(4) else
intervals[3] = [8,10]
newInterval: [3,8]
newInterval[0] > intervals[3][1] → 3 > 10 → False
newInterval = [min(3, 8), max(8, 10)] = [3, 10]. newInterval: [3,10].

(5) if
intervals[4] = [12,16]
newInterval[1] < intervals[4][0] → 10 < 12 → True
Add newInterval = [3, 10] to output
=> output + intervals[i:] = [[1, 2], [3, 10]] + [[12, 16]]

'''

# @lc code=end

