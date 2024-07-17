#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
# https://www.youtube.com/watch?v=9UtInBqnCgA

# @lc code=start


from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            # {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
        for char in countS:
           # if countS[s[char]] != countT[t[char]]: will error if t[char] not exist
            
            if countS[char] != countT.get(char, 0):  #countS[char] =3
                return False

        return True  


    """
    Other solution:

    return sorted(s) == sorted(t)

    or
    
    return Counter(s) == Counter(t)
    
    """


# @lc code=end

