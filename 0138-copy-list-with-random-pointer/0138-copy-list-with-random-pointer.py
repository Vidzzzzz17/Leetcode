from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mapping = {None: None}

        cur = head
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            mapping[cur].next = mapping[cur.next]
            mapping[cur].random = mapping[cur.random]
            cur = cur.next

        return mapping[head]