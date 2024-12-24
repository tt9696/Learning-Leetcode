#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # head = [1 -> 2 -> 3 -> 4 -> 5]
        
        current = head
        prev = None

        while current:
            next_node = current.next # save next_node = 2 -> 3 -> 4 -> 5
            current.next = prev # current.next = 1 -> None
            prev = current # prev= 1-> None
            current = next_node # current = 2 -> 3 -> 4 -> 5
        return prev
    
# @lc code=end
"""
Iteration 1:

Save next_node = 2 -> 3 -> 4 -> 5.
Reverse: current.next = prev → 1 -> None.
Move prev = current → prev = 1 -> None.
Move current = next_node → current = 2 -> 3 -> 4 -> 5.

Iteration 2:
Save next_node = 3 -> 4 -> 5.
Reverse: current.next = prev → 2 -> 1 -> None.
Move prev = current → prev = 2 -> 1 -> None.
Move current = next_node → current = 3 -> 4 -> 5.

Repeat until the end:
Final prev = 5 -> 4 -> 3 -> 2 -> 1 -> None.

-----------------------------------------------------
REcursive
def reverseList(self, head):
        if not head or not head.next:  # Base case
            return head

        reversed_list = self.reverseList(head.next)  # Reverse the rest
        head.next.next = head  # Adjust pointers
        head.next = None       # Disconnect the original link

        return reversed_list   # Return the new head
"""
