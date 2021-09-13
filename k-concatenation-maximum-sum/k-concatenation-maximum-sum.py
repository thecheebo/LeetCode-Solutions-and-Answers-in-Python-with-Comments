class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        def max_sum(lst):
            n = len(lst)
            max_ending_here, max_so_far = lst[0], lst[0]
            for x in lst[1:]:
                max_ending_here = max(max_ending_here + x, x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        if not arr:
            return 0
        s = sum(arr)
        if k == 1:
            return max(0, max_sum(arr)) % (10 ** 9 + 7)
        else:
            return max(0, (k - 2) * max(s, 0) + max_sum(arr + arr)) % (10 ** 9 + 7)