# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levelList = collections.deque()
        res = []
        if root:
            levelList.append(root)

        while levelList:
            qlen = len(levelList)
            for i in range(qlen):
                cur = levelList.popleft()
                if i == qlen - 1:
                    res.append(cur.val)
                if cur.left:
                    levelList.append(cur.left)
                if cur.right:
                    levelList.append(cur.right)
        return res
