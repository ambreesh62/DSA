# Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Definition for a binary tree node.

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        result = []

        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root) 
        
        return result       
