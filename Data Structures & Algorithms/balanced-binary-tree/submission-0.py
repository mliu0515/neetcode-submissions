# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]

    def helper(self, node):
        if not node:
            return True, 0
        isLeftBalanced, leftHeight = self.helper(node.left)
        isRightBalanced, rightHeight = self.helper(node.right)
        return (isLeftBalanced and isRightBalanced and abs(leftHeight - rightHeight) <= 1), max(leftHeight, rightHeight) + 1

