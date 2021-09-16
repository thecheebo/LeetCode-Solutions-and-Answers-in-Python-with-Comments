from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        paths = [1 for _ in range(m)]
        for _ in range(1, n):
            for i in range(1, m):
                paths[i] += paths[i - 1]
        return paths[-1]