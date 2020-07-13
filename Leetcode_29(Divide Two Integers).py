# my solution for Leetcode question 29, Divide Two Integers (without using * / %)


class Solution:
    def divide(self, dividend, divisor):

        uDividend = abs(dividend)
        uDivisor = abs(divisor)
        result = 0

        while uDividend - uDivisor >= 0 or uDivisor != abs(divisor):
            if result >= pow(2, 31) - 1:
                if not self.sameSign(dividend, divisor):
                    return 0 - pow(2, 31)
                return pow(2, 31) - 1
            if uDivisor == abs(divisor):
                temp = 1
            if uDividend - uDivisor < 0:
                temp =0
                uDivisor = abs(divisor)
                continue
            result += temp
            uDividend -= uDivisor
            uDivisor += uDivisor
            temp += temp

        if not self.sameSign(dividend, divisor):
            result = 0 - result

        return result
    
    def sameSign(self, a, b):
        if (a < 0 and b < 0) or (a >= 0 and b >= 0):
            return True
        return False