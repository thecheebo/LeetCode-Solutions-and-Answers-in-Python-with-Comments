# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def solve(root, maxval):
            if not root: 
                return 0, float('inf'), -float('inf')
            left,  minvl, maxvl = solve(root.left, maxval)
            right, minvr, maxvr = solve(root.right, maxval)
            if left == -1 or right == -1 or not maxvl < root.val < minvr:
                return -1, 0, 0
            maxval[0] = max(maxval[0], 1 + left + right)
            return 1 + left + right, min(root.val, minvl, minvr), max(root.val, maxvr, maxvl)
        
        maxval = [0]
        solve(root, maxval)
        return maxval[0]