class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        current = 0
        lastUnrepeatedIndex = 0
        
        dict = {}
        
        for i in range(len(s)):
            if dict.get(s[i]) != None:
                print(lastUnrepeatedIndex)
                current = i - lastUnrepeatedIndex
                lastUnrepeatedIndex = max(dict.get(s[i])+ 1, lastUnrepeatedIndex)
                dict[s[i]] = i
                if current > result:
                    result = current
            else:
                dict[s[i]] = i
                
        print(lastUnrepeatedIndex)
        return max(result, len(s) - lastUnrepeatedIndex)