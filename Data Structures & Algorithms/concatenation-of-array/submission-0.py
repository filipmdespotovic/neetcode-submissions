from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

s = Solution()
print(s.getConcatenation([1, 2, 3, 4]))
