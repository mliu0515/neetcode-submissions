# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        return self.helper(root)[0]
    
    def helper(self, root):
        if root is None:
            return 0, 0
        
        leftDiameter, leftHeight = self.helper(root.left)
        rightDiameter, rightHeight = self.helper(root.right)

        currentDiameter = leftHeight + rightHeight
        bestDiameter = max(leftDiameter, rightDiameter, currentDiameter)

        currentHeight = 1 + max(leftHeight, rightHeight)

        return bestDiameter, currentHeight
        