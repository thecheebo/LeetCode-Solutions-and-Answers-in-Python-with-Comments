class Solution(object):
    def twoSum(self, nums, target):
        
        # Create 
        d = {}
   
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [i, d[m]]
            else:
                d[n] = i
