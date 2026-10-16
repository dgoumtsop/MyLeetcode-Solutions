# Time: O(n), Space: O(1)
# each step moves one pointer inward so at most n steps, and I only store two indices
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # start at both ends of the sorted array
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:   
                return [left + 1, right + 1]
            elif total < target:      
                left += 1
            else:       
                right -= 1
        return []