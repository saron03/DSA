# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        answer = 0
        def dfs(node):
            nonlocal answer
            if not node:
                return (0, 0)  
                
            left_total, left_count = dfs(node.left)
            right_total, right_count = dfs(node.right)

            total = left_total + right_total + node.val
            count = left_count + right_count + 1

            if total // count == node.val:
                answer += 1

            return (total, count)

        dfs(root)
        return answer
