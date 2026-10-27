from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(node, remaining):
            if not node:
                return
            path.append(node.val)
            remaining -= node.val
            if not node.left and not node.right and remaining == 0:
                res.append(path[:])      # copy, since path is mutated later
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)
            path.pop()                   # backtrack

        dfs(root, targetSum)
        return res