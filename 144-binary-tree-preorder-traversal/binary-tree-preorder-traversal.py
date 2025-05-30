# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        def preorder(root):
            if not root:
                return
            arr.append(root.val)
            preorder(root.left)
            preorder(root.right)
        arr = []
        preorder(root)
        return arr

        
        