class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack (day, temp)
        stack = []
        res = [0] * len(temperatures)
        for day, temp in enumerate(temperatures):
            # if non-increasing, add it to the stack
            if not stack or temp <= stack[-1][1]:
                stack.append((day, temp))
            else:
                while stack and temp > stack[-1][1]:
                    res[stack[-1][0]] = day - stack[-1][0]
                    stack.pop()
                stack.append((day, temp))
        return res

        