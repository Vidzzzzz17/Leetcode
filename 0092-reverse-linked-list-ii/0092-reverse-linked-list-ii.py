# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(0, head)
        prev = dummy

        # Move prev to the node just before position `left`
        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next  # first node of the segment (becomes its tail)

        for _ in range(right - left):
            nxt = cur.next          # node to move to the front
            cur.next = nxt.next     # unlink nxt from its current spot
            nxt.next = prev.next    # insert nxt at the front of the segment
            prev.next = nxt

        return dummy.next