# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        traversed = set()
        res = 1

        if root:
            stack.append((root, root.val))
        
        while stack:
            curNode, nodeVal = stack[-1]
            if curNode.left and curNode.left not in traversed:
                if curNode.left.val >= nodeVal:
                    res += 1
                stack.append((curNode.left, max(nodeVal, curNode.left.val)))
            elif curNode.right and curNode.right not in traversed:
                if curNode.right.val >= nodeVal:
                    res += 1
                stack.append((curNode.right, max(nodeVal, curNode.right.val)))
            else:
               traversed.add(curNode)
               stack.pop()


        return res