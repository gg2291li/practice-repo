# my solution for zig-zug leetcode question 6, time complexity is O(n)

class Solution:
    def convert(self, s, numRows) -> str:
        if len(s) == 0: return s

        direction = "down"
        level = 0

        temp = []
        for row in range(numRows):
            temp.append([])
        
        for index in range(len(s)):
            temp[level].append(s[index])
            if level < numRows - 1 and direction == "down":
                level += 1
            elif level == numRows - 1 and direction == "down":
                level -= 1
                direction = "up"
            elif level > 0 and direction == "up":
                level -= 1
            else:
                level += 1
                direction = "down"

        result = ""

        for row in temp:
            for letter in row:
                result += letter

        return result
