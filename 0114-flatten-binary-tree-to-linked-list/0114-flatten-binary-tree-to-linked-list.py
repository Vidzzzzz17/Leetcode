from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                # find the rightmost node of the left subtree
                pred = cur.left
                while pred.right:
                    pred = pred.right
                # attach the original right subtree after it
                pred.right = cur.right
                # move the left subtree to the right
                cur.right = cur.left
                cur.left = None
            cur = cur.right