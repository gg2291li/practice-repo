# the solution for Question 4 on Leetcode, but the time complexity is O(m + n) instead of O(log(m + n)), which is slower than the asked solution

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        if len(nums1) == 0:
            return self.median(nums2)
        if len(nums2) == 0:
            return self.median(nums1)

        nums = []
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                nums.append(nums2[j])
                j += 1
            elif j == len(nums2):
                nums.append(nums1[i])
                i += 1
            else:
                if nums1[i] < nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
        
        return self.median(nums)


    def median(self, s):
        n = len(s)
        return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None