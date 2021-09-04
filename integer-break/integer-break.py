class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))
        return dp[n]

'''
████████████ PROBLEM ████████████
Given an integer n, break it into the sum of k positive integers, 
where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

████████████ EXAMPLE ████████████
Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


████████████ EDGE ████████████

████████████ BRUTE ████████████
This approach is a bottom up dynamic programming solution. We are going to have an array called dp where dp[i] will correspond to the maximum product of breaking number i into a sum of k positive integers. For each number i we are going to break it into two parts. The ways in which we can break i into two parts is by subtracting j from i, where j < i. So the two parts we will get will be i-j and j. Now we think to ourselves: 'I just split i into two parts, namely i-j and j, and I have already found the maximum product for each of those parts. Ok, so now let me consider each of the following: 1.) I multiply i and i-j. 2.) I multiply the the maximum product I found for part j and i-j. 3.) I multiply the the maximum product I found for part i-j and j.' 4.) I multiply the the maximum product I found for part j and the maximum product I found for part i-j.' Now we set dp[i] to be the max of those four products we took into consideration. We then return dp[n], the maximum product of breaking number n into a sum of k positive integers.

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))
        return dp[n]
████████████ OPTIMIZE ████████████
5
initalte array for n+1

████████████ PSEUDO ████████████

████████████ CODE 

████████████ EDGE ████████████

████████████ REFRACTOR ████████████

''' 