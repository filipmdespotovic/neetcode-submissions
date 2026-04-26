from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}
        for i in range(0, len(nums)):
            x = nums[i]            
            if x not in dicti:
                dicti[x] = []
            dicti[x].append(i)
        
        for broj in dicti.keys():
            r = target - broj
            if r == broj:
                if len(dicti[r]) > 1:
                    return [dicti[broj][0], dicti[broj][1]]    
                else:
                    continue
            if r in dicti:                
                return [dicti[broj][0], dicti[r][0]]
                

s = Solution()
print(s.twoSum([1, 3, 4, 2], 6))