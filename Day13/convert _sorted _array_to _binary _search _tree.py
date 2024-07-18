# Convert Sorted Array to Binary Search Tree
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sorted_array_to_bst(self, nums: int) -> TreeNode:
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        root.left = self.sorted_array_to_bst(nums[:mid])
        root.right = self.sorted_array_to_bst(nums[mid + 1:])
        
        return root
    
def print_tree(root: TreeNode, depth=0, prefix="Root: "):
    if not root:
        print(" " * (depth * 4) + prefix + "None")
        return
    
    print(" " * (depth * 4) + prefix + str(root.val))
    if root.left or root.right:
        print_tree(root.left, depth + 1, "L--- ")
        print_tree(root.right, depth + 1, "R--- ")

# Example usage
nums = [-10, -3, 0, 5, 9]
solution = Solution()
bst_root = solution.sorted_array_to_bst(nums)
print_tree(bst_root)