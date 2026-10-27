from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        pre = 0  # next root to take from preorder

        def build(lo, hi):
            nonlocal pre
            if lo > hi:
                return None
            root = TreeNode(preorder[pre])
            pre += 1
            mid = idx[root.val]
            root.left = build(lo, mid - 1)    # left subtree comes first in preorder
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)