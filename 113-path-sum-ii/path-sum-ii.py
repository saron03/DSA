# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []

        def dfs(root, arr, currSum):
            if not root:
                return
            currSum += root.val
            if root.left is None and root.right is None:
                if currSum == targetSum:
                    ans.append(arr + [root.val])
                return

            dfs(root.left, arr + [root.val], currSum)
            dfs(root.right, arr + [root.val], currSum)

        dfs(root, [], 0)
        return ans