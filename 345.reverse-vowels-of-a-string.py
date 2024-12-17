#
# @lc app=leetcode id=345 lang=python
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Input: s = "leetcode"
        # Output: "leotcede"
        vowels = set('aeiouAEIOU')
        s = list(s) # Convert string to list to modify it in-place
        
        left ,right = 0 , len(s) -1

        while left < right:
            if s[left] not in vowels:
                left += 1 # move left pointer
                continue
           
            if s[right] not in vowels:
                right -= 1 # move right pointer
                continue
            
            # Swap the vowels
            s[left], s[right] = s[right], s[left]

            # Move both pointers
            left += 1
            right -= 1
        
        return ''.join(s) # Convert list back to string
# @lc code=end

