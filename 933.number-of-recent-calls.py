#
# @lc app=leetcode id=933 lang=python
#
# [933] Number of Recent Calls
#

# @lc code=start
from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)
    
    # Example usage
    # recentCounter = RecentCounter()
    # print(recentCounter.ping(1))  # returns 1
    # print(recentCounter.ping(100))  # returns 2

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end
"""
Step 1: ping(1)
Current Timestamp (t): 1
Queue before adding: []
Add the timestamp (1) to the queue: The queue becomes [1].
Remove outdated timestamps: No timestamps are outdated because there are no previous pings.
Queue after removal: [1]
Return the count of recent pings (within 3000 ms): The queue has 1 element, so the result is 1.
Queue: [1]

Step 2: ping(100)
Current Timestamp (t): 100
Queue before adding: [1]
Add the timestamp (100) to the queue: The queue becomes [1, 100].
Remove outdated timestamps: No timestamps are outdated because 100 - 3000 is negative, and 1 is still within the 3000 ms window.
Queue after removal: [1, 100]
Return the count of recent pings (within 3000 ms): The queue has 2 elements, so the result is 2.
Queue: [1, 100]

"""
