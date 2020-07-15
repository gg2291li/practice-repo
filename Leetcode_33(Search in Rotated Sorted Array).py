# My solution for question 33, Search in Rotated Sorted List
# Using Binary Search with modified conditions

class Solution:
    def search(self, nums, target):
        if nums ==[]: return -1
        lIndent = 0
        rIndent = len(nums) - 1

        while True:
            mid = (rIndent - lIndent) // 2
            if rIndent - lIndent <= 1:
                if nums[lIndent] == target: return lIndent
                if nums[rIndent] == target: return rIndent
                return -1
            if nums[lIndent + mid] == target:
                return lIndent + mid
            else:
                if target < nums[mid + lIndent] and (nums[lIndent] > nums[mid + lIndent] or target > nums[lIndent]):
                    rIndent = rIndent - mid - 1
                elif target < nums[mid + lIndent]:
                    lIndent = lIndent + mid + 1
                elif target > nums[mid + lIndent] and  (nums[rIndent] < nums[mid + lIndent] or target < nums[rIndent]):
                    lIndent = lIndent + mid + 1
                else:
                    rIndent = rIndent - mid - 1
