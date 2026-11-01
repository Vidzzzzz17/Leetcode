class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        leftmost = root
        while leftmost and leftmost.left:
            cur = leftmost
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            leftmost = leftmost.left
        return root