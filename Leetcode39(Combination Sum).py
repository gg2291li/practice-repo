class Solution:
    def combinationSum(self, candidates, target):
        if candidates == []: return []
        result = []
        self.helper(candidates, result, [], 0, target)
        return result
    
    def helper(self, candidates, result, answer, summ, target):
        if summ == target:
            result.append(answer)
            return
        if summ > target:
            return
        if candidates == []:
            return
        for i in range(len(candidates)):
            self.helper(candidates[i:], result, answer + [candidates[i]], summ+candidates[i], target)
