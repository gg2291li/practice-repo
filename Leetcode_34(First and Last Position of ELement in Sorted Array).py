class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0: return [-1, -1]
        lIndent = 0
        rIndent = len(nums) - 1

        while True:
            if rIndent - lIndent <= 1:
                if nums[lIndent] == target and nums[rIndent] == target: return [lIndent, rIndent]
                if nums[lIndent] == target: return [lIndent, lIndent]
                if nums[rIndent] == target: return [rIndent, rIndent]
                return [-1, -1]
            
            if (nums[lIndent] == target and nums[rIndent] == target) and (lIndent == 0 or nums[lIndent - 1] < target) and (rIndent == len(rIndent) - 1 and nums[rIndent + 1] > target):
                return [lIndent, rIndent]
            
