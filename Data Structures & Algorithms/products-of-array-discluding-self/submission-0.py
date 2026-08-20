class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        res2 = [1] * len(nums)
        for i in range(0, len(nums) - 1):    
            res[i + 1] = res[i] * nums[i]
        
        for j in range(len(nums) - 1, 0, -1):
            res2[j - 1] = res2[j] * nums[j]

        for k in range(len(res)):
            res[k] *= res2[k]
        
        print(res)
        print(res2)
        
        return res