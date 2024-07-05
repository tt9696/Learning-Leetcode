#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
# abcabcbb => abc (not repeat)

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set() #Initialize a set to store characters of the current window.
        left = 0 
        max_length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left]) #remove until the duplicate removed
                left +=1
            char_set.add(s[right])
            max_length = max(max_length, right-left+1)
        return max_length
        
    """
    string "abcabcbb":
    Substrings without repeating characters:

    "abc"
    "bca"
    "cab"
    "abc"
    "b"
    "bb" (has repeating characters, so it's not considered)
    "b" (repeats already considered characters)

    "pwwkew"
    wke
    kew
    wwk : no
    pwke :no ,answer must be a substring,

    add(s[right] {'p'}
    add(s[right] {'p', 'w'}
    remove p
    after remove become {'w'}
    remove w
    after remove become set()
    add(s[right] {'w'}
    add(s[right] {'k', 'w'}
    add(s[right] {'e', 'k', 'w'} or  {'e', 'w', 'k'} or {'w', 'k', 'e'}
    remove w
    after remove become {'e', 'k'}
    add(s[right] {'e', 'k', 'w'} 
    """
# @lc code=end

