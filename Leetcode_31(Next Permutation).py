# My solution for Leetcode question 31, Next Permutation
# My logic is to find the first (going reverse in the list) item that can be changed to satisfy lexicographical order
# Then after the swap, I rearrange the items in between the two swapped items to increasing order

class Solution:
    def nextPermutation(self, nums):
        temp = ""
        lst = []
        for index in range(len(nums) - 1, -1, -1):
            if lst == [] or self.allLess(nums[index], lst):
                lst.append(nums[index])
            else:
                for lstIndex in range(len(lst)):
                    if nums[index] < lst[lstIndex]:
                        temp = nums[index]
                        nums[index] = lst[lstIndex]
                        lst[lstIndex] = temp
                        lst.sort()
                        i = 0
                        for ind in range(index + 1, len(nums)):
                            nums[ind] = lst[i]
                            i += 1
                        return

        for index in range(len(nums)):
            if index < len(nums) - index - 1:
                temp = nums[index]
                nums[index] = nums[len(nums) - index - 1]
                nums[len(nums) - index - 1] = temp

        return

    def allLess(self, num, lst):
        for each in lst:
            if num < each:
                return False
        return True