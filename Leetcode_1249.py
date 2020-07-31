class Solution:
    def minRemoveToMakeValid(self, s):
        stack = []
        for index in range(len(s)):
            if index >= len(s):
                break
            if s[index] == ')':
                if stack == []:
                    s = s[0:index] + s[index + 1:]
                    index -= 1
                else:
                    stack.pop()
            elif s[index] == '(':
                stack.append(index)

        count = 0
        for item in stack:
            s = s[0: item - count] + s[item + 1 - count:]
            count += 1
        return s