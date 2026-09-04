import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = ( left + right) // 2
            hr = 0
            for pile in piles:
                hr += math.ceil(pile/mid)
            if hr <= h:
                right = mid
            else:
                left = mid + 1
        return left