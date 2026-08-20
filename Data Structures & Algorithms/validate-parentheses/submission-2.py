class Solution:
    def isValid(self, s: str) -> bool:
        correctPair = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in correctPair:
                stack.append(char)
            else:
                if len(stack) == 0 or correctPair[stack[-1]] != char:
                    return False
                stack.pop()
        return len(stack) == 0