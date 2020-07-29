class Solution:
    def permute(self, nums):
        if nums == []: return []
        return self.helper(nums, [])

    def helper(self, nums, result):
        if result == []:
            result = [[nums[0]]]
            nums = nums[1:]
        tempResult = []

        for num in nums:
            for res in result:
                for index in range(len(res) + 1):
                    temp = res[:]
                    temp.insert(index, num)
                    tempResult.append(temp)
            result = tempResult[:]
            tempResult = [] 
        return result
        