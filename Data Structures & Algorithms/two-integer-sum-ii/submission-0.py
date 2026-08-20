class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head, tail = 0, len(numbers) - 1
        while head != tail:
            curTotal = numbers[head] + numbers[tail]
            if curTotal == target:
                return [head + 1, tail + 1]
            if curTotal > target:
                tail -= 1
            else:
                head += 1
        return [head + 1, tail + 1]
