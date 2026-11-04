# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(tree):
            if not tree:
                return True, float('inf'), float('-inf')
        
            isLeftValid, leftMin, leftMax = helper(tree.left)
            isRightValid, rightMin, rightMax = helper(tree.right)
            return (isLeftValid and isRightValid and leftMax < tree.val and rightMin > tree.val), min(leftMin, rightMin, tree.val), max(leftMax, rightMax, tree.val)
        
        return helper(root)[0]