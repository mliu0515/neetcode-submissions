class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        l = len(nums)

        nums.sort()
        def dfs(i):
            if i >= l:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i + 1)

            val = cur.pop()
            while i < l and nums[i] == val:
                i += 1
            dfs(i)

        dfs(0)

        return res