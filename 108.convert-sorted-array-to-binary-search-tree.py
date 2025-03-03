#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        
        # BT - The left child is smaller than the parent, The right child is greater than the parent, The left and right subtrees must also be BSTs.
        # [-10,-3,0,5,9]
        middle = len(nums) // 2 # choose middle as root # 5 // 2 = 2
        root = TreeNode(nums[middle]) # Create the root node TreeNode(0)

        #Recursively build the left subtree from the left half and the right subtree from the right half.
        root.left = self.sortedArrayToBST(nums[:middle]) # Left part: [-10, -3]
        root.right = self.sortedArrayToBST(nums[middle+1:]) # Right part: nums[3:] = [5, 9]

        return root

"""
[-10, -3]
Middle is -3.
Left child of 0 is -3.
Left subtree → [-10]
No right subtree.

nums = [5, 9]
Middle is 9.
Right child of 0 is 9.
Left subtree → [5]
No right subtree.

Final Tree
      0
     / \
   -3   9
   /   /
 -10  5

"""

# @lc code=end

