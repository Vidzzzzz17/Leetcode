from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # length of list
        n, node = 0, head
        while node:
            n += 1
            node = node.next

        dummy = ListNode(0, head)
        size = 1
        while size < n:
            prev, cur = dummy, dummy.next
            while cur:
                left = cur
                right = self._split(left, size)   # cut off first `size` nodes
                cur = self._split(right, size)    # cut off next `size` nodes
                prev = self._merge(left, right, prev)
            size *= 2
        return dummy.next

    def _split(self, node, size):
        """Detach the first `size` nodes; return the head of the remainder."""
        for _ in range(size - 1):
            if not node:
                break
            node = node.next
        if not node:
            return None
        rest = node.next
        node.next = None
        return rest

    def _merge(self, a, b, prev):
        """Merge sorted lists a and b after `prev`; return the new tail."""
        tail = prev
        while a and b:
            if a.val <= b.val:
                tail.next, a = a, a.next
            else:
                tail.next, b = b, b.next
            tail = tail.next
        tail.next = a or b
        while tail.next:
            tail = tail.next
        return tail