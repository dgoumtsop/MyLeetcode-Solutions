class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # time complexity O(1) loop thru the array once
        # space complexity O(1) constant use of memory
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

        