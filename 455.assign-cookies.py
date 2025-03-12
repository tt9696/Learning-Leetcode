#
# @lc app=leetcode id=455 lang=python
#
# [455] Assign Cookies
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # g -> Children’s Greed Factor, Each child has a minimum cookie size they need to be happy.
        # s -> Available Cookie Sizes, s = [1, 1], it means: You have two cookies, both of size 1

        # Goal: You want to maximize the number of happy children.
        # A child is happy if they get a cookie greater than or equal to their greed factor.

        # Sort the lists to match smallest children to smallest cookies.
        g.sort()
        s.sort()
        i, j = 0 , 0  # i → children, j → cookies

        happy_count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]: # Cookie can satisfy child
                happy_count += 1
                i += 1 # Move to next child
            j += 1 # Move to next cookie
        return happy_count

# @lc code=end

"""
Step 1: Sorting
Sorted g: [1, 2]
Sorted s: [1, 2, 3]

Step 2: Assign Cookies
The first child needs at least 1. ✅ Give them s[0] = 1. (Happy 🎉)
The second child needs at least 2. ✅ Give them s[1] = 2. (Happy 🎉)
Final Answer: 2 children are happy.

✅ Output → 2

"""

