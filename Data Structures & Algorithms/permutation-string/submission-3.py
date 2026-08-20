class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Decode = [0] * 26
        s2Decode = [0] * 26
        for c in s1:
            curIndex = ord(c) - ord('a')
            s1Decode[curIndex] += 1
        
        l, r = 0, 0
        while l <= r and r < len(s2):
            curChar = s2[r]
            s1CharCount = s1Decode[ord(curChar) - ord('a')]
            if s1CharCount == 0:
                while l < r:
                    leftChar = s2[l]
                    if s1Decode[ord(leftChar) - ord('a')] != 0:
                        s2Decode[ord(leftChar) - ord('a')] -= 1
                    l += 1
                l = r + 1
                r += 1
                continue
            while s2Decode[ord(curChar) - ord('a')] >= s1CharCount and l <= r:
                leftChar = s2[l]
                if s1Decode[ord(leftChar) - ord('a')] != 0:
                    s2Decode[ord(leftChar) - ord('a')] -= 1
                l += 1

            s2Decode[ord(curChar) - ord('a')] += 1
            if s1Decode == s2Decode:
                return True
            r += 1

        return False
