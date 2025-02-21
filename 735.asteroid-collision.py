#
# @lc app=leetcode id=735 lang=python
#
# [735] Asteroid Collision
#        Positive: moving right, Negative: moving left.

# @lc code=start
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            # stack = [5, 10]
            while stack and asteroid < 0 < stack[-1]:
                # Collision occurs
                if -asteroid > stack[-1]: #-5 negative asteroid is larger and destroys the top asteroid in the stack
                    # Current asteroid destroys the top of the stack
                    stack.pop() # -5 is destroyed.
                    continue
                elif -asteroid == stack[-1]:
                    # Both asteroids destroy each other
                    stack.pop()
                break
            else:
                stack.append(asteroid) # positive,  No collision or asteroid moving right
        return stack
# @lc code=end
"""
Inside the while loop:
Check if -asteroid > stack[-1]:

-(-5) = 5 and stack[-1] = 10.
5 > 10 is false, so this block is skipped.
Check elif -asteroid == stack[-1]:

-(-5) = 5 and stack[-1] = 10.
5 == 10 is false, so this block is also skipped.
break

"""

