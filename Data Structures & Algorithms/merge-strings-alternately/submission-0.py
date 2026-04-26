class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = ""

        i = 0
        j = 0

        while i < len(word1):
            sol += word1[i]
            i += 1
            if j < len(word2):
                sol += word2[j]
                j += 1
        
        while j < len(word2):
                sol += word2[j]
                j += 1

        return sol