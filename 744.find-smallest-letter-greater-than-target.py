#
# @lc app=leetcode id=744 lang=python
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """ 
        # letters = ["c", "f", "j"], target = c
        for letter in letters: 
            if letter > target: #'f' > 'c' → ✅ 
                return letter #return f
        return letters[0] # wrap around, letters = ["x","x","y","y"], target = "z", no greater so return x
        
# @lc code=end
"""
Binary Search
def nextGreatestLetter(letters, target):
    left, right = 0, len(letters)

    while left < right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return letters[left % len(letters)]


"""
