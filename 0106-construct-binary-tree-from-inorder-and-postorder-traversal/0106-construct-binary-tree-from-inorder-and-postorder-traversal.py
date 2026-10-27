from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        post = len(postorder) - 1  # next root to take, reading postorder backwards

        def build(lo, hi):
            nonlocal post
            if lo > hi:
                return None
            root = TreeNode(postorder[post])
            post -= 1
            mid = idx[root.val]
            root.right = build(mid + 1, hi)   # right subtree comes first when reading backwards
            root.left = build(lo, mid - 1)
            return root

        return build(0, len(inorder) - 1)