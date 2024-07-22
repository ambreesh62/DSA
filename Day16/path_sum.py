# Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def has_path_sum(self, root: TreeNode, targetSum: int) -> bool:
        if not sum:
            return False

        targetSum -= root.val

        if not root.left and not root.right:  # if leaf node
            return targetSum == 0
        
        return self.has_path_sum(root.left, targetSum) or self.has_path_sum(root.right, targetSum)

# Example usage:
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

solution = Solution()
print(solution.has_path_sum(root, 22))  # Example targetSum