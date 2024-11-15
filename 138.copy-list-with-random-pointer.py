#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Hash Map
# https://www.youtube.com/watch?v=5Y2EiZST97Y
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        old_to_new = {}
        current = head
        # Step 1: Create a mapping from old nodes to new nodes
        while current:
            old_to_new[current] = Node(current.val) #old_to_new[Node1] = Node(7)
            current = current.next  

        # Step 2: Assign next and random pointers
        current = head
        while current:
            if current.next: # original node’s next pointer
                old_to_new[current].next = old_to_new[current.next]   
            if current.random: #original node’s random pointer
                old_to_new[current].random = old_to_new[current.random]
            current = current.next

        return old_to_new[head]
            # old_to_new = {
            # Node1: Node1' (val=7),
            # Node2: Node2' (val=13),
            # Node3: Node3' (val=11)
        # } it doesn't provide any information about the random pointers
        # Expected Output Format: [node_value, random_pointer_index]  
        # head (which points to Node1 (val=7)) =>[[7,null],[13,0],[11,4],[10,2],[1,0]]
        
# @lc code=end
"""
First Loop
Original List:
Node1 (val: 7) -> Node2 (val: 13) -> Node3 (val: 11)

#old_to_new dictionary has created deep copies of all the nodes but has not set their next or random pointers yet.
old_to_new = {
    Node1: Node1' (val=7, next=None, random=None),
    Node2: Node2' (val=13, next=None, random=None),
    Node3: Node3' (val=11, next=None, random=None)
}
Second loop
Iteration 1: Process Node1 
old_to_new[Node1].next = old_to_new[Node1.next] => Node1'.next = Node2'
random=None

Iteration 2: Process Node2
Node2'.next = Node3'
old_to_new[Node2].random = old_to_new[Node2.random] => Node2'.random = Node1'

Iteration 3: Process Node3
Node3.next = None
Node3'.random = Node2'

||
V
 old_to_new = {
    Node1: Node1' (val=7, next=Node2', random=None),
    Node2: Node2' (val=13, next=Node3', random=Node1'),
    Node3: Node3' (val=11, next=None, random=Node2')
}
"""
