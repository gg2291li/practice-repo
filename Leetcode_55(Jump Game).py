class Solution:
    def canJump(self, nums):
        if nums == []: return True
        frthest = 0
        dsti = len(nums) - 1
        for index in range(len(nums)):
            if frthest < index:
                return False
            elif frthest >= dsti:
                return True
            else:
                if index + nums[index] > frthest:
                    frthest = index + nums[index]

        return False