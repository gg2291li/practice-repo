# My solution for Leetcode question 17, Letter Combinations of a Phone number
# Place all the necessary mappings of dights to letter in a dictionary, then update the result while iterating through the input "digits" list

class Solution:
    def letterCombinations(self, digits):
        digitToLetter = {0:[], 1:[], 2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], 5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], 8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}

        if len(digits) < 1: return []
        result = [""]
        for digit in digits:
            if digit in ['0', '1']: return []
            current = result
            result = []
            for letter in digitToLetter[int(digit)]:
                for element in current:
                    result.append(element + letter)
        
        return result