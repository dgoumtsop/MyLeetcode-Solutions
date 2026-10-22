class Solution:
    def maxArea(self, h: List[int]) -> int:
        # time complexity O(n) only move 1 step inward
        # space complexity 0(1) no extra step
        l, r = 0, len(h) - 1
        maxWater = 0
        while l < r:
            area = min(h[l], h[r]) * (r - l)
            maxWater = max(maxWater, area)
            if h[l] < h[r]:
                l+=1
            else:
                r-=1
        return maxWater
            
        

        
        