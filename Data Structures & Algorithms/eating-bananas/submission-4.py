import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            ch = 0
            print(l,r)
            mid = l + ((r-l) // 2)
            for pile in piles:
                ch += math.ceil(pile/mid)
            if ch > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res