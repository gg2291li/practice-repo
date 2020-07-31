class Solution:
    def subarraySum(self, nums, k):
        if nums == []: return 0
        result = 0
        sum = 0
        hashSum = {}
        for num in nums:
            sum += num
            hashSum[sum] = True

        sum = 0
        if hashSum.get(k) == True:
            print("run")
            result = 1

        for num in nums:
            sum += num
            if hashSum.get(k + sum) == True:
                print("2")
                result += 1
             
        return result