class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        nums = [i for i in range(1,10)]
        def backtrack(index, current, remainder):
            if remainder == 0 and len(current) == k:
                result.append(current[:])
            for i in range(index, 10):
                if remainder - i < 0:
                    continue
                current.append(i)
                backtrack(i + 1, current, remainder - i)
                current.pop()
                
        result = []
        backtrack(index = 1, current = [], remainder = target)
        return result
            
            
            