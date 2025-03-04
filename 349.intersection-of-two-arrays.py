#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)
    # return list(set(nums1).intersection(set(nums2)))
    """
    set1 = {4,9,5}
    set2 = {9,4,8}
    Intersection → {4,9}
    Convert to list → [4,9] ✅
    """
        
# @lc code=end

"""
Using Sorting & Two Pointers
nums1.sort()
nums2.sort()

i, j = 0, 0
result = set()

while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        result.add(nums1[i])
        i += 1
        j += 1
    elif nums1[i] < nums2[j]:
        i += 1
    else:
        j += 1

    return list(result)

"""