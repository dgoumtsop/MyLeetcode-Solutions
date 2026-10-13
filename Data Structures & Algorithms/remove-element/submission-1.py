class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # time complexity O(n) since we loop thru the arr once
        # space complexity O(1) only use a constant amount of mem
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        