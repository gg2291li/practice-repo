class Solution:
    def groupAnagrams(self, strs):
        if strs == []: return []
        strsDict = {}
        strsCopy = strs[:]
        result = []
        for index in range(len(strsCopy)):
            strsCopy[index] = "".join(sorted(strsCopy[index]))
        for index in range(len(strsCopy)):
            if strsDict.get(strsCopy[index]):
                continue
            else:
                temp = []
                for ind in range(index + 1, len(strsCopy)):
                    temp.append(strs[ind])
                    if strsCopy[index] == strsCopy[ind]:
                        temp.append(strs[ind])
                    result.append(temp)
                    temp = []
                strsDict[strsCopy[index]] = True
        return result