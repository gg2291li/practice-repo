# My solution for Leetcode question 16, 3 Sum Closest, using two pointer method


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for index in range(len(nums) - 2):
            lo = index + 1
            hi = len(nums) - 1

            while lo != hi:
                if abs(target - result) > abs(target - nums[index] - nums[lo] - nums[hi]):
                    result = nums[index] + nums[lo] + nums[hi] 
                if nums[index] + nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    hi -= 1

        return result
