# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelList = deque()
        res = []
        if root:
            levelList.append(root)
        
        while levelList:
            curLevel = []
            for _ in range(len(levelList)):
                cur = levelList.popleft()
                if cur:
                    curLevel.append(cur.val)
                    if cur.left:
                        levelList.append(cur.left)
                    if cur.right:
                        levelList.append(cur.right)
            if curLevel:
                res.append(curLevel)    
        return res