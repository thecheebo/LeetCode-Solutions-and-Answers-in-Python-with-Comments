class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        N = len(coins)
        if N == 0:
            if amount == 0:
                return 1
            return 0

        dp = [[0]*(amount+1) for _ in range(N)]
        for i in range(N):
            dp[i][0] = 1

        for i in range(N):
            for j in range(1, amount+1):
                
                dp[i][j] = dp[i-1][j]
                
                #if the j value(representing CURRENT amount) is at least the size of the current coin.
                if j - coins[i] >= 0:
                    
                    #check
                    dp[i][j] += dp[i][j-coins[i]]




        return dp[-1][-1]   
'''
███████████████████████████████████ PROBLEM ███████████████████████████████████ 
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of 
money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

INPUT: integer array, integer amount
OUTPUT: integer(combinations)

███████████████████████████████████ EXAMPLE ███████████████████████████████████ 
♦ Example 1:

    Input: amount = 5, coins = [1,2,5]
    Output: 4

    Explanation: there are four ways to make up the amount:
    5=5
    5=2+2+1
    5=2+1+1+1
    5=1+1+1+1+1
    
♦ Example 2:

    Input: amount = 3, coins = [2]
    Output: 0

Explanation: the amount of 3 cannot be made up just with coins of 2.

♦ Example 3:

    Input: amount = 10, coins = [10]
    Output: 1

███████████████████████████████████ EDGE ███████████████████████████████████ 

███████████████████████████████████ BRUTE ███████████████████████████████████ 
■ backtracking, + count every time you hit target


███████████████████████████████████ OPTIMAL ███████████████████████████████████ 
■ 2d dp 
███████████████████████████████████ PSEUDO ███████████████████████████████████ 

███████████████████████████████████ CODE ███████████████████████████████████ 

        N = len(coins)
        if N == 0:
            if amount == 0:
                return 1
            return 0

        dp = [[0]*(amount+1) for _ in range(N)]
        for i in range(N):
            dp[i][0] = 1

        for i in range(N):
            for j in range(amount):
                dp[i][j+1] = dp[i-1][j+1]
                if j+1 - coins[i] >= 0:
                    dp[i][j+1] += dp[i][j+1-coins[i]]




        return dp[-1][-1]   
███████████████████████████████████ TEST ███████████████████████████████████ 
'''