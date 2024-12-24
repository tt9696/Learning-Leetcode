#
# @lc app=leetcode id=2215 lang=python
#
# [2215] Find the Difference of Two Arrays
#

# @lc code=start
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        #  Hash Sets Approach
        unique1 = set()
        unique2 = set()

        for num in nums1:
            if num not in nums2:
                unique1.add(num) # {1, 3}

        for num in nums2:
            if num not in nums1:
                unique2.add(num) # {4, 6}

        return [list(unique1), list(unique2)]
        
# @lc code=end

"""
Approach : Using Sets
def findDifference(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

Approach : Without Sets
def findDifference(self, nums1, nums2):
        unique1 = []
        unique2 = []

        # Find unique elements in nums1 not in nums2
        for num in nums1:
            if num not in nums2 and num not in unique1:
                unique1.append(num)

        # Find unique elements in nums2 not in nums1
        for num in nums2:
            if num not in nums1 and num not in unique2:
                unique2.append(num)

        return [unique1, unique2]

"""