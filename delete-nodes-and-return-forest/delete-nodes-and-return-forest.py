# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        to_delete = set(to_delete)
        res = []
        def walk(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = walk(root.left, parent_exist=False)
                root.right = walk(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = walk(root.left, parent_exist=True)
                root.right = walk(root.right, parent_exist=True)
                return root
        walk(root, parent_exist=False)
        return res
        
'''
██████████████████████████████████► PROBLEM ◄██████████████████████████████████

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest 
(a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the 
result in any order.

██████████████████████████████████► EXAMPLE ◄███████████████████████████████████  
Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

██████████████████████████████████► EDGE ◄███████████████████████████████████  



██████████████████████████████████► BRUTE ◄███████████████████████████████████ 


██████████████████████████████████► OPTIMAL ◄███████████████████████████████████  
██████████████████████████████████► PSEUDO ◄███████████████████████████████████  
██████████████████████████████████► CODE ◄███████████████████████████████████  
██████████████████████████████████► TEST ◄███████████████████████████████████  




'''