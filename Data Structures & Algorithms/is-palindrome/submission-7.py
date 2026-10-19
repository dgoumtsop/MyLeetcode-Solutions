class Solution:
    def isPalindrome(self, s: str) -> bool:
        # time complexity O(n)
        # space complexity O(n)
        clean = ''.join(c.lower() for c in s if c.isalnum())
        return clean == clean[::-1]
        