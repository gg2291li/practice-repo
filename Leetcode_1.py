# python solution with 2-pass hashmap for Leetcode question "Two Sums"


class Solution:
    def twoSum(self, nums, target):
        numsDict = {}

        for index in range(len(nums)):
            if (numsDict.get(nums[index]) != None) and (target / 2 == nums[index]):
                return [numsDict[nums[index]], index]
            else:
                numsDict[nums[index]] = index

        for index in range(len(nums)):
            if numsDict.get(target - nums[index]) != None and (target /2 != nums[index]):
                return [index, numsDict[target - nums[index]]]
        
