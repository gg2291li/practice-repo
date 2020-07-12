# My solution for Leetcode question 20, Valid Parentheses
# I used stack to push/pop to check whether the input is valid

class Solution:
    def isValid(self, s):
        stack = []
        for item in s:
            if item in ['(', '[', '{']:
                stack.append(item)
            elif item == ')':
                if stack == [] or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif item == ']':
                if stack == [] or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else:
                if stack == [] or stack[-1] != '{':
                    return False
                else:
                    stack.pop()

        if stack == []: return True

        return False

        