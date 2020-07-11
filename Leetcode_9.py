# My solution for leetcode question 9, Palindrome Number
# convert the number to string then check if the string is a palidrome

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        for index in range(len(string_x)):
            if (string_x[index] != string_x[len(string_x) - index - 1]):
                return False
        
        return True
