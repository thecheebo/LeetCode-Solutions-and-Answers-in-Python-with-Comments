# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(s, t):
            # helper function that does the actual subtree check
            if (s is None) and (t is None):
                return True
            if (s is None) or (t is None):
                return False
            return (s.val == t.val and check(s.left, t.left) and check(s.right, t.right))

        # need to do a pre-order traversal and do a check
        # for every node we visit for the subtree
        if not root:
            # return False since None cannot contain a subtree 
            return False
        if check(root, subRoot):
            # we found a match
            return True
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            # a match was found
            return True
        return False
