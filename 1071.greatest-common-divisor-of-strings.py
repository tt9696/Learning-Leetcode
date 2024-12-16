#
# @lc app=leetcode id=1071 lang=python
#
# [1071] Greatest Common Divisor of Strings
# https://www.youtube.com/watch?v=i5I_wrbUdzM

# @lc code=start
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)

        # If str1 + str2 is not equal to str2 + str1, no common divisor string exists
        if str1 + str2 != str2 + str1:
            return "" #"LEETCODE" != "CODELEET"
        
        # Checks if a substring of length l can be a divisor of both str1 and str2.
        def isDivisor(l):
            # len1 % l == 0, this means that l can evenly divide len1
            # len2 % l == 0, this means that l can evenly divide len2
            if len1 % l or len2 % l: #check can evenly divide-checks if either len1 % l != 0 or len2 % l != 0
                return False #if one of these != 0 it, return False
            
            f1, f2 = len1 // l, len2 // l # factor
            # check whether a substring of length l can be repeated to form the entire strings str1 and str2
            if str1[:l] * f1 == str1 and str2[:l] * f2 == str2:
                return True

        for l in range(min(len1,len2),0,-1):# Decreases l by 1 with each iteration backwards, 0 — The loop will stop before it reaches 0
            #for min(9, 6) = 6 and go down to 1. So, it will check for l = 6, l = 5, l = 4, l = 3, l = 2, and l = 1.
            if isDivisor(l):
                return str1[:l]
        return ""
        
      
        
# @lc code=end

