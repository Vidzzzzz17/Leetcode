from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)      # head of the sorted list
        tail = dummy             # last node of the sorted list
        cur = head

        while cur:
            nxt = cur.next       # save before relinking

            if tail is dummy or tail.val <= cur.val:
                # fast path: cur belongs at the end
                tail.next = cur
                tail = cur
            else:
                # find the insertion point
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                cur.next = prev.next
                prev.next = cur

            cur = nxt

        tail.next = None         # terminate the list
        return dummy.next