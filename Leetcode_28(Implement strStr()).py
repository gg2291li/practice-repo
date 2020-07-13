# my solution for question 28, implement strStr()

class Solution():
    def strStr(self, haystack, needle):
        n = len(needle)

        if needle == "": return 0

        for i in range(len(haystack) - n + 1):
            if needle == haystack[i: i + n]:
                return i

        return -1