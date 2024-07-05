#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        # shortest = min(strs,key=len)

        # for i, char in enumerate(shortest):# 0 f 1 l 2 o 3 w
        #     for word in strs:
        #         #print("word",word)
        #         #print("word[i]",word[i]) # f f f l l l o o i 
        #         if word[i] != char: #i
        #             #print("shortest[:i]",shortest[:i]) #fl
        #             return shortest[:i]
        
        # return shortest
        
        sortedList = sorted(strs) #    ['flight', 'flow', 'flower']

        first = sortedList[0] 
        last = sortedList[-1]
        ans = ""
        # 6, 6 
        for i in range(min(len(first), len(last))): #0,1,2,3,4,5,
            if(first[i] == last[i]):
                ans += first[i]
            else:
                break
        
        return ans

        
# @lc code=end

