#
# @lc app=leetcode id=1629 lang=python
#
# [1629] Slowest Key
# Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
# Output: "c"
# Explanation: The durations are [9,20,20,1]. 
# Keys 'b' and 'c' are both pressed for 20 units. 
# 'c' is lexicographically larger.


# @lc code=start
class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        durations = [releaseTimes[0]]
        for i in range(1, len(releaseTimes)):
            durations.append(releaseTimes[i]- releaseTimes[i-1])

        max_duration = max(durations)# two 20
        candidate = [] 

        for i in range(len(durations)):
            if durations[i] == max_duration:
                candidate.append(keysPressed[i])# b, c

        return max(candidate) # Return lexicographically largest key

# @lc code=end
"""
max_duration = releaseTimes[0]
slowest = keysPressed[0]

for i in range(1, len(releaseTimes)):
    duration = releaseTimes[i] - releaseTimes[i-1]
    if duration > max_duration or (duration == max_duration and keysPressed[i]> slowest):
        max_duration = duration
        slowest = keysPressed[i]

return slowest

"""
