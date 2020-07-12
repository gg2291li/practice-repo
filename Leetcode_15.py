# My solution for Leetcode question 15, 3 sum, a bit slow, but gets the job done
# The time complexity is O(N^2), using hashmap to find the 3rd value

class Solution:
    def threeSum(self, nums):
        indexDict = {}
        result = []
        tempi = ["placeholder"]
        tempj = ["placeholder"]

        if len(nums) < 3: return []

        nums.sort()

        for index in range(len(nums)):
            indexDict[nums[index]] = index

        for i in range(len(nums) - 2):
            if nums[i] == tempi:
                continue
            for j in range(i + 1, len(nums) - 1):
                if nums[j] == tempj:
                    continue
                if indexDict.get(0 - nums[i] - nums[j]) not in [None, i, j] and indexDict.get(0 - nums[i] - nums[j]) > i and indexDict.get(0 - nums[i] - nums[j]) > j:
                    result.append([nums[i], nums[j], nums[indexDict.get(0 - nums[i] - nums[j])]])
                tempj = nums[j]
            tempi = nums[i]

        return result
