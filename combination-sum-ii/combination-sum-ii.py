class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(current, remainder, index):
            
            if remainder == 0:
                unique_combinations.append(current[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if (remainder - candidates[i] >= 0):
                    current.append(candidates[i])

                    backtrack(current, remainder - candidates[i], i+1)

                    current.pop()

                else:
                    break
            

        
        
        unique_combinations = []
        
        
        backtrack([],target, 0)
        return unique_combinations