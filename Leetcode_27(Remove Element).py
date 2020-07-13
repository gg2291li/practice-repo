# My solution for Leetcode question 27, Remove Element, solution is very similar to question 26

class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0: return 0

        position = 0

        for index in range(len(nums)):
            if nums[index] != val:
                nums[position] = nums[index]
                position += 1
        return position