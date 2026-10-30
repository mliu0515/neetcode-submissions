class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(curStr, leftNum, rightNum):
            # two choices, add a left one (if possible), or close the parenthesis
            if leftNum == n and rightNum == n:
                res.append(curStr)
                return
            if leftNum < n:
                helper(curStr + "(", leftNum + 1, rightNum)
            if rightNum < leftNum:
                helper(curStr + ")", leftNum, rightNum + 1)
            else:
                return

        
        helper("", 0, 0)

        return res