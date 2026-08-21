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
        i = 0

        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i: j])
            i = j
        return res

