class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            # TODO: the final case of some sort
            timeTook = self.totalHours(piles, mid)
            if timeTook > h:
                # means we need a faster speed
                l = mid + 1
            else:
                res = mid
                # see we can see if we can go even slower
                r = mid - 1
        
        return res

    def totalHours(self, piles, speed):
        res = 0
        for p in piles:
            res += math.ceil(float(p) / speed)
        return res
        