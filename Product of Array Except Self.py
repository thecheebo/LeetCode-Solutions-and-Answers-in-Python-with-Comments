

"""
https://leetcode.com/problems/product-of-array-except-self/
Brute Force Method
Big (O)n^2 
"""

class Solution(object):
    def productExceptSelf(self, nums):
        answer = [None]*len(nums)
        for i in range(len(nums)):
            counter = 1
            for j in range(len(nums)):
                if i != j:
                    counter *= nums[j]
            answer[i] = counter
        return answer
        
        
"""

(O)n 
