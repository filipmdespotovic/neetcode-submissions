from typing import List
class Solution:
    def svi_isti(self, lista: List[int]) -> bool:
        prvi = lista[0]
        for x in lista:
            if x != prvi:
                return False
        return True
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sol = ""

        n = len(strs[0])
        for s in strs:
            if n > len(s):
                n = len(s)

        dict = {}
        
        for ind in range(0, n):
            for s in strs:
                if ind not in dict:
                    dict[ind] = []
                dict[ind].append(s[ind])

        for i in dict.keys():
            if self.svi_isti(dict[i]):
                sol += dict[i][0]
            else:
                break

        return sol