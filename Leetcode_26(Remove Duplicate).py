# My solution for Leetcode question 26, Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0: return 0
        current = "placeholder"
        position = 0

        for index in range(len(nums)):
            if nums[index] != current:
                nums[position] = nums[index]
                current = nums[index]
                position += 1
        return position