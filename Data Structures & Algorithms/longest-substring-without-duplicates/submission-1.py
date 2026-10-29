class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strSet = set()
        res = 0

        l, r = 0, 0
        while l <= r and r < len(s):
            while s[r] in strSet:
                if s[l] in strSet:
                    strSet.remove(s[l])
                    l += 1
            strSet.add(s[r])
            r += 1
            res = max(res, len(strSet))
        
        return res