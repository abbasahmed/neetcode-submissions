class Solution:
    def isPalindrome(self, s: str) -> bool:
        pt1 = 0
        pt2 = len(s) - 1

        while pt1 < pt2:
            while pt1 < pt2 and not s[pt1].isalnum():
                pt1 += 1
            while pt1 < pt2 and not s[pt2].isalnum():
                pt2 -= 1
            if s[pt1].lower() != s[pt2].lower():
                return False
            pt1 += 1
            pt2 -= 1
        
        return True