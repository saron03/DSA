# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        symmetric = True
        def checker(left,right):
            nonlocal symmetric
            if not left and not right:
                return 
            if not left or not right:
                symmetric = False
                return
            if left.val != right.val:
                symmetric = False
                return
            checker(left.left,right.right)
            checker(left.right, right.left)
        
        checker(root.left,root.right)
        return symmetric
            


        
        