# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        def reverse(left,right,level):
            if not left:
                return 
            if level % 2 !=0:
                left.val, right.val = right.val,left.val
            reverse(left.left,right.right,level+1)
            reverse(left.right,right.left,level+1)

        reverse(root.left,root.right,level+1)
        return root