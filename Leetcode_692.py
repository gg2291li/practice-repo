class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if words == [] or k == 0: return []
        
        words.sort()
        oldWord = ""
        count = 0
        countWords = []
        for word in words:
            if word != oldWord:
                countWords.append([oldWord, count])
                oldWord = word
                count = 1
            else:
                count += 1
        
        countWords.append([oldWord, count])
        
        countWords.sort(key=lambda p:p[1], reverse = True)
        
        result = []
        for i in range(k):
            result.append(countWords[i][0])
        print(countWords)
        
        return result