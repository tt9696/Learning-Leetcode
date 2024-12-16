#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move `prev` to the node before position `left`
        for _ in range(left-1):
            prev = prev.next # prev = 1

        current = prev.next #current = 2

        # Reverse the sublist
        for _ in range(right-left):  # 0, 1, 2
            temp = current.next # temp -> 3
            current.next = temp.next # current.next -> 4
            temp.next = prev.next # temp.next -> 2
            prev.next = temp # prev.next -> 3

        return dummy.next
# @lc code=end

"""
head = [1, 2, 3, 4, 5], left = 2, right = 4

Initial State:
prev → 1
curr → 2
Sublist to reverse: [2, 3, 4]

First Iteration:
temp = curr.next: temp → 3
curr.next = temp.next: List becomes 1 -> 2 -> 4 -> 5, and temp → 3.
temp.next = prev.next: temp.next → 2 (current reversed portion).
prev.next = temp: List becomes 1 -> 3 -> 2 -> 4 -> 5.

Second Iteration:
temp = curr.next: temp → 4
curr.next = temp.next: List becomes 1 -> 3 -> 2 -> 5, and temp → 4.
temp.next = prev.next: temp.next → 3 (current reversed portion).
prev.next = temp: List becomes 1 -> 4 -> 3 -> 2 -> 5.

Final State:
The sublist [2, 3, 4] is now reversed to [4, 3, 2].
"""