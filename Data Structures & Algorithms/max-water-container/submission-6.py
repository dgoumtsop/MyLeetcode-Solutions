class Solution:
    def maxArea(self, h: List[int]) -> int:
        # time complexity O(n) only move 1 step inward
        # space complexity 0(1) no extra step
        left, right = 0, len(h) - 1
        maxWater = 0
        while left < right:
            area = min(h[left], h[right]) * (right - left)
            maxWater = max(maxWater, area)
            if h[left] < h[right]:
                left+=1
            else:
                right-=1
        return maxWater

            
        

        
        