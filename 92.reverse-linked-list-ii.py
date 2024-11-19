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

        # dummy -> 1 -> 2 -> 3 -> 4 -> 5

        # Step 2: Start the reversal process
        start = prev.next # start = 2
        then = start.next # then = 3

        # Reverse the sublist
        # left = 2, right = 4
        for _ in range(right-left): # 0, 1, 2
            start.next = then.next
            then.next = prev.next 
            prev.next = then 
            then = start.next 

        return dummy.next
        
# @lc code=end

"""
head = [1, 2, 3, 4, 5], left = 2, right = 4

dummy -> 1 -> 2 -> 3 -> 4 -> 5
         |    |    |
        prev start then

prev = dummy, prev =1, start = 2, then = 3

First Iteration:
then = 3 => dummy -> 1 -> 3 -> 2 -> 4 -> 5
then = start.next # 4 

Second Iteration:
then = 4 => dummy -> 1 -> 4 -> 3 -> 2 -> 5
then = start.next # 5 

End:
The sublist [2, 3, 4] is now reversed.

Output : [1, 4, 3, 2, 5]

start = 2, then = 3, prev = 1

Step 1: start.next = then.next (Update start.next to point to 4)
dummy -> 1 -> 2    3 -> 4 -> 5
                \
                 -> 4

Step 2: then.next = prev.next (Update then.next to point to prev.next 3 -> 2 (which is 2)
dummy -> 1 -> 3 -> 2    4 -> 5

Step 3: prev.next = then (Update prev.next to point to then (which is 3))
dummy -> 1 -> 3 -> 2 -> 4 -> 5

Step 4: then = start.next
Move then to start.next, which is 4.

"""