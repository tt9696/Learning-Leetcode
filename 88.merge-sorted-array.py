#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        
        for x in range(len(nums1)):
            if i>=n:
                break
            if nums1[x] == 0:
                nums1[x] = nums2[i]
                i+=1
        nums1.sort()
        
        # Sample Answer: 
        # nums1[m:] = nums2[:] 
        # nums1.sort()

        # nums1[m:] refers to the slice of the list nums1 starting from the index m to the end of the list. 
        # eg. nums1[2:], which means the sublist [3, 4, 5]. original = [1, 2, 3, 4, 5]
        # nums2[:] refers to the entire list nums2.
# @lc code=end

