#using expansion from middle, this is my solution for question 5 on leetcode

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s

        result = ""
        temp = ""


        for center in range(len(s)):
            temp = s[center]
            i = 1
            while (center + i < len(s) and center - i >= 0 and s[center + i] == s[center - i]):
                temp = s[center + i] + temp + s[center + i]
                i += 1
            if len(temp) > len(result):
                result = temp

        temp = ""
        for center in range(len(s) - 1):
            if (s[center] == s[center +1]):
                temp = s[center] + s[center + 1]
            else:
                continue
            i = 1
            while (center + 1 + i < len(s) and center - i >= 0 and s[center + 1 + i] == s[center - i]):
                temp = s[center - i] + temp + s[center - i]
                i += 1
            if len(temp) > len(result):
                result = temp


        return result