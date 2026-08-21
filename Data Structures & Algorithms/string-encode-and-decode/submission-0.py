class Solution:

    def encode(self, strs: List[str]) -> str:
        # I think it's all about recording the delimiter
        # Can't just simply combine, because the string itself can contain comma, or any other puncuation
        finalStr = ""
        for s in strs:
            strLen = len(s)
            finalStr += str(strLen) + "*" + s
        return finalStr

    def decode(self, s: str) -> List[str]:
        res = []
        curLen = ""
        curStr = ""

        idx = 0
        while idx < len(s):
            curChar = s[idx]
            if curChar == "*":
                for _ in range(int(curLen)):
                    idx += 1
                    curStr += s[idx]
                res.append(curStr)
                curLen = ""
                curStr = ""
            else:
                curLen += curChar
            idx += 1
        return res

