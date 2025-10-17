# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        def compare(node):
           
            if not node.left and not node.right:
                return 1
            if not node.left:
                return 1 + compare(node.right)
            if not node.right:
                return 1 + compare(node.left)
            return 1 + min(compare(node.left), compare(node.right))
            
        return compare(root)