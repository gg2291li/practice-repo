# My solution to Leetcode question 22, Generate Parentheses
# Using DFS approach 

class Solution:
    def generateParenthesis(self, n):
        self.ans = []
        self.dfs('', n, n)
        return self.ans
        
    def dfs(self, pre, left, right):
        if right == 0:
            self.ans.append(pre)
        if left:
            self.dfs(pre + '(', left - 1, right)
        if right > left:
            self.dfs(pre + ')', left, right - 1)