"""
https://leetcode.com/problems/coin-change


Dynamic Programming

"""

class Solution(object):
    def coinChange(self, coins, amount):
        
        dp_array = [amount+1] * (amount + 1)
        dp_array[0] = 0

        for coin in coins:
            for count in range(coin, amount+1):
                dp_array[count] = min(dp_array[count], dp_array[count-coin]+1)
        if dp_array[amount] != (amount + 1):
            return dp_array[amount]
        return -1
