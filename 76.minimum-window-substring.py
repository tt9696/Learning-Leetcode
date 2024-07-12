#
# @lc app=leetcode id=76 lang=python
#
# [76] Minimum Window Substring
# https://www.youtube.com/watch?v=jSto0O4AJbM

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        countT = {}
        window = {}
        if t == "" : return ""

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
            #  countT =  {'A': 1, 'B': 1, 'C': 1}

        have , need = 0, len(countT)
        res = [-1,-1]
        resLength = float("infinity")
        left = 0
        for right in range(len(s)):
            c = s[right] # A
            window[c] = 1 + window.get(c, 0)
            # window = {'A': 1}
            # countT contains two 'A's but window[c] only has one 'A', 
            # it means that the current window does not yet satisfy 
            # the requirement for 'A'. 
            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need:
                if (right - left + 1) < resLength: # # Update result
                    res = [left, right]
                    resLength = right - left + 1

                # pop the the first left in window
                window[s[left]] -= 1 
                if s[left] in countT and window[s[left]] < countT[s[left]]:# when t contain two A, but window have one A
                    have -= 1
                left += 1 #move left pointer to next

        left, right = res
        return s[left:right + 1] if resLength != float("infinity") else ""

        
# @lc code=end

