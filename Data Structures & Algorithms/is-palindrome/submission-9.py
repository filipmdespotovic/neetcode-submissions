class Solution:
    def isAlpha(self, s: str) -> bool:
        if (s >= 'A' and s <= 'Z') or (s >= 'a' and s<= 'z') or (s >= '0' and s <= '9'):
            return True
        return False


    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while not self.isAlpha(s[i]) and i < j:
                i += 1
            while not self.isAlpha(s[j]) and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        
        return True