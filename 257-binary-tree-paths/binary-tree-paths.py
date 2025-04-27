# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traversal(root, path):
            if not root:
                return
            if not root.left and not root.right:
                arr.append("->".join(path))
            if root.left:
                traversal(root.left, path + [str(root.left.val)])
            if root.right:
                traversal(root.right,path + [str(root.right.val)])
        arr = []
        traversal(root,[str(root.val)])
        return arr
            