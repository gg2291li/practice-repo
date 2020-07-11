# answer for leetcode question 7, straight forward python solution. Python uses memory to store integer bits, 
# it doesn't have the problem of integer overflow unless memory itself isn't enough

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        negative = False if x >= 0 else True
        current = -x if negative else x

        while (current != 0):
            result = result * 10 + current % 10
            current = current // 10

        result = -result if negative else result

        if result < pow(-2, 31) or result > pow(2, 31) - 1:
            result = 0

        return result