# My solution for Leetcode 14, Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) < 1: return ""

        result = strs[0]

        for str in strs:
            temp = ""
            for position in range(len(str)):
                if position >= len(result) or str[position] != result[position]:
                    break
                else:
                    temp += str[position]
            result = temp

        return result