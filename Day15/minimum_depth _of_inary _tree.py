#  Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def min_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return self.min_depth(root.right) + 1
        
        if not root.right:
            return self.min_depth(root.left) + 1
        
        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1
