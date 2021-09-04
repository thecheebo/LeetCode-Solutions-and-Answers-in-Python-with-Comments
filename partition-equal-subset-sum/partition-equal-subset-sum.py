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
        target = total_sum / 2
        partial_sums = {0}
        for num in nums:
            temp_set = partial_sums.copy()
            for partial in partial_sums:
                temp_set.add(partial + num)
            #partial_sums.add()
            partial_sums = temp_set    
        return True if target in partial_sums else False
           
        
        