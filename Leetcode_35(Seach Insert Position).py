class Solution:
    def searchInsert(self, nums, target):
        if len(nums) == 0: return 0
        lBound = 0
        rBound = len(nums) - 1

        while True:
            mid = (rBound - lBound) // 2
            if target == lBound + mid: return lBound + mid
            # test 1