#
# @lc app=leetcode id=2032 lang=python
#
# [2032] Two Out of Three
#

# @lc code=start
from collections import Counter
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1) # {1, 2, 3}
        set2 = set(nums2) # {2, 3}
        set3 = set(nums3) # {3}
        count = Counter(set1) + Counter(set2) + Counter(set3) # count = Counter({3: 3, 2: 2, 1: 1})
        result = []
        for num, freq in count.items():
            if freq >=2 :
                result.append(num)
        # result = [num for num, freq in count.items() if freq >= 2]
        return result # result = [3, 2]

# @lc code=end

"""
ret = []

ret += set(nums1).intersection(set(nums2))
ret += set(nums1).intersection(set(nums3))
ret += set(nums2).intersection(set(nums3))

result = list(set(ret))    
return result
"""