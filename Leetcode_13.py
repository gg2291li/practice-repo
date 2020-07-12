# My solution for Leetcode 13, Roman to Integer.
# Straight forward solution, checking if any character needs to be minused instead of added 

class Solution:
    def romanToInt(self, s: str) -> int:
        valueList = {'M': 1000,
                     'D': 500,
                     'C': 100,
                     'L': 50,
                     'X': 10,
                     'V': 5,
                     'I': 1}

        result = 0
        value = 0
        for item in s:
            result += valueList[item]
            if value != 0 and valueList[item] > value:
                result -= (value * 2)

            value = valueList[item]

        return result