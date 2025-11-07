class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node, path):
            if node is None:
                return

            path += str(node.val)

            if not node.left and not node.right:
                ans.append(path)
                return
            path += "->"
            dfs(node.left, path)
            dfs(node.right, path)
            
        dfs(root, "")
        return ans
