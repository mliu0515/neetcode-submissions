class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l, r = 0, 0
        res = 0
        while r < len(s) and l <= r:
            i = s[r]
            count[ord(i) - ord('A')] += 1
            while r - l + 1 - max(count) > k and l <= r:
                j = s[l]
                count[ord(j) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


        