#
# @lc app=leetcode id=2095 lang=python
#
# [2095] Delete the Middle Node of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        # head = 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
        dummy = ListNode(0) # dummy -> 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
        dummy.next = head
        slow = dummy
        fast = head

        # Traverse the list until fast reaches the end
        while fast and fast.next:
            slow = dummy.next # slow moves 1 step
            fast = head.next.next # fast moves 2 steps
        
        # fast reach the end of list, means slow reach before middle node
        # fast reach 6, slow reach 4
        # link slow.next to 1 (slow.next.next)
        slow.next = slow.next.next

        return dummy.next  # Return the head of the modified list
# @lc code=end

