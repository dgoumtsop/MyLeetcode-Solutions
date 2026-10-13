class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time complexity O(nlgn) sorting
        # space complexity O(n) create new list
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        