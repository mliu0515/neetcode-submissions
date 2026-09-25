# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal
        res = []

        def inOrder(tree):
            if len(res) == k:
                return
            if not tree:
                return 
            if tree.left:
                inOrder(tree.left)
            res.append(tree.val)
            if tree.right:
                inOrder(tree.right)
        
        inOrder(root)
        if res:
            return res[k - 1]
