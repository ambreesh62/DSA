#  Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)
        return max(left_depth, right_depth) + 1


def create_tree_from_list(list):
    if not list:
        return None

    root = TreeNode(list[0])
    nodes = [root]
    i = 1
    while i < len(list):
        node = nodes.pop(0)
        if node:
            if i < len(list) and list[i] is not None:
                node.left = TreeNode(list[i])
                nodes.append(node.left)
            i += 1
            if i < len(list) and list[i] is not None:
                node.right = TreeNode(list[i])
                nodes.append(node.right)
            i += 1
    return root


# Example
tree_list = [3, 9, 20, None, None, 15, 7]
root = create_tree_from_list(tree_list)
solution = Solution()
print(solution.max_depth(root))  # Output 3
