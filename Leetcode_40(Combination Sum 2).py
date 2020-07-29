class Solution:
    def combinationSum2(self, candidates, target):
        if candidates == []: return []
        candidates.sort()
        res = []
        self.helper(candidates, res, [], 0, target)
        result = []
        for i in res:
            if i not in result:
                result.append(i)
        return result
    
    def helper(self, candidates, result, answer, suum, target):
        if suum > target:
            return
        if suum == target:
            result.append(answer)
            return
        if candidates == []:
            return
        for i in range(len(candidates)):
            self.helper(candidates[i+1:], result, answer + [candidates[i]], suum + candidates[i], target)