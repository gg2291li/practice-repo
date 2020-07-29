class Solution:
    def searchInsert(self, nums, target):
        if len(nums) == 0: return 0
        lBound = 0
        rBound = len(nums) - 1

        while True:
            mid = (rBound - lBound) // 2
            if target == nums[lBound + mid]: return lBound + mid
            elif target < nums[lBound + mid]:
                if lBound + mid == 0 or target > nums[lBound + mid -1]:
                    return lBound + mid
                else:
                    rBound = lBound + mid - 1
            else:
                if lBound + mid == len(nums) - 1 or target < nums[lBound + mid + 1]:
                    return lBound + mid + 1
                else:
                    lBound = lBound + mid + 1
            # test 5