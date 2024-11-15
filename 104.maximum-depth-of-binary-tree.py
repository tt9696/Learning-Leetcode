#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
# https://www.youtube.com/watch?v=hTM3phVI6YQ&t=701s

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Approach 1 : Iterative BFS - Breadth First Search, queue
        """
        from collections import deque
        
        if not root:
            return 0
        
        queue = deque([root]) # nodes are dequeued (popped from the left of the deque), 
        # and their child nodes are enqueued (appended to the right of the deque).
        depth = 0
        while queue:
            level = len(queue)
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            depth += 1
        return depth
        """
        # Approach 2 : Recursive DFS 
       
        if root is None:
            return 0
        # Recursively calculate the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The maximum depth is the larger of the two, plus 1 for the current node
        return 1 + max(left_depth, right_depth)
        
        """
        # Approach 3 : Iterative DFS 
        stack = [(root, 1)] # (node, depth)
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node :
                max_depth = max(max_depth,depth)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return max_depth
        """
# @lc code=end

    """
    Approach 1 : Iterative BFS - Breadth First Search, queue
    Initial: deque([3])
    Processing the root (level 1):          Dequeue 3. Enqueue 3's children (9 and 20)--> queue = deque([9, 20])
    Processing the left child (level 2):    Dequeue 9. Enqueue 9's children (it has none, so nothing is added). queue = deque([20])
    Processing the right child (level 2):   Dequeue 20.Enqueue 20's children (15 and 7).
    Processing the left grandchild (level 3):Dequeue 15.Enqueue 15's children (it has none, so nothing is added).queue = deque([7]).
    Processing the right grandchild (level 3):Dequeue 7.Enqueue 7's children (it has none, so nothing is added).queue = deque([]).
    ----------------------------------------------------------------------
    Approach 2 : Recursive DFS 
    Start at root 3:
    Call maxDepth(root.left) for 9.
    Call maxDepth(root.right) for 20.
    
    Left subtree (9):
    maxDepth(9.left) = 0 (null).
    maxDepth(9.right) = 0 (null).
    Depth at 9 = 1 + max(0, 0) = 1.
    
    Right subtree (20):
    Call maxDepth(20.left) for 15.
    Call maxDepth(20.right) for 7.
    
    Subtree (15):
    maxDepth(15.left) = 0 (null).
    maxDepth(15.right) = 0 (null).
    Depth at 15 = 1 + max(0, 0) = 1.

    Subtree (7):
    maxDepth(7.left) = 0 (null).
    maxDepth(7.right) = 0 (null).
    Depth at 7 = 1 + max(0, 0) = 1.
    
    Back to 20:
    Depth at 20 = 1 + max(1, 1) = 2.
    Back to root 3:
    Depth at 3 = 1 + max(1, 2) = 3.
    ----------------------------------------------------------------------  

    Approach 3 : Iterative DFS 
    stack = [(3, 1)]
    Pop (3, 1), max_depth = max(0, 1) = 1 => Push children stack = [(9, 2), (20, 2)]
    Pop (20, 2), max_depth = max(1, 2) = 2 => stack = [(9, 2), (15, 3), (7, 3)]
    Pop (7, 3), max_depth = max(2, 3) = 3 => stack = [(9, 2), (15, 3)]
    Pop (15, 3), max_depth = max(3, 3) = 3 => stack = [(9, 2)]
    Pop (9, 2) , max_depth = max(3, 2) = 3 => stack = []
    
    For general-purpose maximum depth calculation, Recursive DFS is the simplest and often sufficient.
    For trees with unknown or potentially large depth, Iterative DFS is safer.
    For level-order-specific tasks or very wide trees, Iterative BFS is preferred.
    """