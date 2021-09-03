class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(index, k):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
                return

            for i in range(index, n):

                # add nums[i] into the current combination
                curr.append(nums[i])

                # use next integers to complete the combination
                backtrack(i + 1, k)

                # backtrack
                curr.pop()
        curr = []
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack(0, k)
        return output