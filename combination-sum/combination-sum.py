class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(current, remainder, index):
            
            if remainder == 0:
                unique_combinations.append(current[:])
                return
            for i in range(index, len(candidates)):
                if (remainder - candidates[i] >= 0):
                    current.append(candidates[i])

                    backtrack(current, remainder - candidates[i], i)

                    current.pop()

                else:
                    break
            

        
        
        unique_combinations = []
        
        
        backtrack([],target, 0)
        return unique_combinations
    
    '''
    
    2           3   6  7   
                ↓   ↓  ↓
    2           x   x  y 
    ↓     ↓
    2     3
    ↓ ↓   ↓ 
    2 3   X
    ↓ Y
    X
    '''