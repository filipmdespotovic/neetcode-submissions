
from typing import *
class Solution:
    def majorityElement(self, nums: List[int]) -> int:                
        nums.sort()        
        x = 0
        broj = -1
        t = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                t += 1
            else:
                if t > x:
                    x = t
                    broj = nums[i - 1]
                    t = 1        
        if t > x:
            x = t
            broj = nums[len(nums) - 1]
            t = 1

        return broj


        