#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
# 

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Floyd's Tortoise and Hare algorithm :Two-pointer technique, 
# where two pointers (slow and fast) traverse the linked list at different speeds. 
# If there is a cycle, the fast pointer will eventually catch up to the slow pointer.
#
#  https://youtube.com/watch?v=gBTe7lFR3vc
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next: # not null
            slow = slow.next        # Move slow by 1 step
            fast = fast.next.next   # Move fast by 2 steps
            if slow == fast:
                return True # Cycle detected
            
        return False #    # No cycle
# @lc code=end

