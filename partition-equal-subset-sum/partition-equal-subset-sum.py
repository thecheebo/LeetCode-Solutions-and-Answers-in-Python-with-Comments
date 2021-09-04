'''
████████████ PROBLEM ████████████
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

████████████ EXAMPLE ████████████
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

████████████ EDGE ████████████
empty arrays? are they nums? valid inputs?
k always less then n?
k can be positive (doesnt say so)


████████████ BRUTE ████████████
try every combination
sum it up
2^n
for every num
to include and not include 
O(n)

████████████ OPTIMIZE ████████████

████████████ PSEUDO ████████████
sum it
if remainder != 0
return false

████████████ CODE 

████████████ EDGE ████████████

████████████ REFRACTOR ████████████

'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2: return False
        subset_sum = total_sum // 2
        
         # construct a dp table of size (subset_sum + 1)
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for curr in nums:
            for j in range(subset_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]

        return dp[subset_sum]