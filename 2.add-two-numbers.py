#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
# https://www.youtube.com/watch?v=wgFPrzTjm7s

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()  # Dummy node to start the result list dummy -> ListNode(val=0, next=None)
        current = dummy # Pointer for the result list
        carry = 0

        while l1 or l2 or carry: # to handle any remaining carry-over
            # Get the current values of l1 and l2, if they exist
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10 # calculates how many tens are in total, carry = 15 // 10 = 1
            current.next = ListNode(total % 10)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        # dummy was initialized with a value of 0
        # if return dummy: dummy -> ListNode(val=0) -> ListNode(val=7) -> ListNode(val=0) -> ListNode(val=8)
        # dummy.next: ListNode(val=7) -> ListNode(val=0) -> ListNode(val=8)

# @lc code=end
"""
l1: 2 -> 4 -> 3 (which represents 342)
l2: 5 -> 6 -> 4 (which represents 465)
Iteration 1
Current Nodes: l1 points to 2, and l2 points to 5.
Add Values: Sum 2 + 5 + carry (which is 0), giving 2 + 5 = 7.
New Carry: The sum is less than 10, so the carry remains 0.
Create New Node: Create a new node with value 7 (total % 10), and link it to current.next.
Move Pointers: Advance l1 to the next node (4), l2 to the next node (6), and current to the newly created node.
Result so far: 7

Iteration 2
Current Nodes: l1 points to 4, and l2 points to 6.
Add Values: Sum 4 + 6 + carry (which is 0), giving 4 + 6 = 10.
New Carry: Since the sum is 10, set carry to 1.
Create New Node: Create a new node with value 0 (total % 10), and link it to current.next.
Move Pointers: Advance l1 to the next node (3), l2 to the next node (4), and current to the newly created node.
Result so far: 7 -> 0

Iteration 3
Current Nodes: l1 points to 3, and l2 points to 4.
Add Values: Sum 3 + 4 + carry (which is 1), giving 3 + 4 + 1 = 8.
New Carry: Since the sum is 8, set carry to 0.
Create New Node: Create a new node with value 8 (total % 10), and link it to current.next.
Move Pointers: Advance l1 and l2 to null, and current to the newly created node.
Result so far: 7 -> 0 -> 8


Check remaining carry in while loop:
If l1 represents 9 -> 9 -> null (which is 99)
And l2 represents 1 -> null (which is 1)
The sum is 100, represented as 0 -> 0 -> 1.
l1 and l2 are both null, but carry is still 1.
"""

