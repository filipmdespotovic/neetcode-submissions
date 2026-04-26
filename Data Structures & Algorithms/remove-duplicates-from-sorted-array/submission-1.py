class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1

        k = 1
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                k += 1
                i += 1
                nums[i] = nums[j]
                j += 1
                
        return k