# Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def is_mirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                (left.val == right.val)
                and is_mirror(left.right, right.left)
                and (left.left, right.right)
            )
        return is_mirror(root.left, root.right) if root else True