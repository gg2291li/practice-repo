# my solution for Leetcode question 19, Four Sum
# The time complexity is O(N^3) as I used 3 nested loops with a hashmap to look for the 4th value
# One alternative is to use 3 pointers, which would yield similar time complexity O(N^3)

class Solution:
    def fourSum(self, nums, target):
        indexDict = {}
        nums.sort()

        result = []
        tempi = "placeholder"
        tempj = "placeholder"
        tempk = "placeholder"

        for index in range(len(nums)):
            indexDict[nums[index]] = index
        

        for i in range(len(nums) - 3):
            if nums[i] == tempi: continue
            tempi = nums[i]
            tempj = "placeholder"
            for j in range(i+1, len(nums) - 2):
                if nums[j] == tempj: continue
                tempj = nums[j]
                tempk = "placeholder"
                for k in range(j+1, len(nums) - 1):
                    if nums[k] == tempk: continue

                    if indexDict.get(target - nums[i] - nums[j] - nums[k]) and indexDict.get(target - nums[i] - nums[j] - nums[k]) > k:
                        result.append([nums[i], nums[j], nums[k], target - nums[i] - nums[j] - nums[k]])
                    tempk = nums[k]
        
        return result