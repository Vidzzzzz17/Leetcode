from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # count the nodes
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        node = head  # next list node to be consumed, in sorted order

        def build(lo, hi):
            nonlocal node
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            left = build(lo, mid - 1)       # in-order: left subtree first
            root = TreeNode(node.val)       # then the current list node
            node = node.next
            root.left = left
            root.right = build(mid + 1, hi) # then the right subtree
            return root

        return build(0, n - 1)