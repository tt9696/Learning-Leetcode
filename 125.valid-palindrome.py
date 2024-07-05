#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = [char.lower() for char in s if char.isalnum()]
        #Example of characters that are not alphanumeric: (space)!#%&? etc.
        return string == string[::-1]
    
        # string[start:stop:step]
        # start: Not specified, so defaults to the start of the string.
        # stop: Not specified, so defaults to the end of the string.
        # step: -1, meaning the slice moves backwards.
    
    """
    txt = "Company 12"
    x = txt.isalnum() # False
    
    txt=s.lower()
    a=re.sub(r'[^a-z0-9]','',txt)
    b=a[::-1]
    """
# @lc code=end

