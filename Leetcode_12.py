# my solution for question 12 of leetcode (integer to Roman), by storing all the cases into a list

class Solution:
    def intToRoman(self, num: int) -> str:
        valueList = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]

        result = ""
        while num != 0:
            for value in valueList:
                while num >= value[1]:
                    result = result + value[0]
                    num -= value[1]

        return result