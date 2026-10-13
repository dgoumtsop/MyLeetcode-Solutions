class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # time complexity O(n) avg to build a set
        # space complexity O(n) worst case
        return len(set(nums)) < len(nums)
        