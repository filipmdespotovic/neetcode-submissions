from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for x in s:
            if x in map1:
                map1[x] += 1
            else:
                map1[x] = 1
        
        for x in t:
            if x in map2:
                map2[x] += 1
            else:
                map2[x] = 1

        return map1 == map2