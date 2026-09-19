class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        cur = []

        def dfs(numSet):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for n in nums:
                if n not in numSet:
                    cur.append(n)
                    numSet.add(n)
                    dfs(numSet)

                    cur.pop()
                    numSet.remove(n)
        dfs(set())

        return res

        