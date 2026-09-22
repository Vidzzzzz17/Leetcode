class Node:
    __slots__ = ('remain', 'prod')
    def __init__(self):
        self.remain = [0] * 5
        self.prod = 1

class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree = [Node() for _ in range(4 * self.n)]
        self._build(nums, 0, 0, self.n - 1)

    def _merge(self, left: Node, right: Node) -> Node:
        res = Node()
        res.prod = (left.prod * right.prod) % self.k
        
        # Prefixes ending in the left child
        for r in range(self.k):
            res.remain[r] = left.remain[r]
            
        # Prefixes ending in the right child, combined with left.prod
        for r in range(self.k):
            res.remain[(r * left.prod) % self.k] += right.remain[r]
            
        return res

    def _build(self, nums: list[int], cur: int, l: int, r: int):
        if l == r:
            val = nums[l] % self.k
            self.tree[cur].remain[val] = 1
            self.tree[cur].prod = val
            return
        
        mid = (l + r) // 2
        self._build(nums, 2 * cur + 1, l, mid)
        self._build(nums, 2 * cur + 2, mid + 1, r)
        self.tree[cur] = self._merge(self.tree[2 * cur + 1], self.tree[2 * cur + 2])

    def update(self, idx: int, val: int):
        val %= self.k
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, cur: int, l: int, r: int, idx: int, val: int):
        if l == r:
            self.tree[cur].remain = [0] * self.k
            self.tree[cur].remain[val] = 1
            self.tree[cur].prod = val
            return
        
        mid = (l + r) // 2
        if idx <= mid:
            self._update(2 * cur + 1, l, mid, idx, val)
        else:
            self._update(2 * cur + 2, mid + 1, r, idx, val)
            
        self.tree[cur] = self._merge(self.tree[2 * cur + 1], self.tree[2 * cur + 2])

    def query(self, ql: int, qr: int) -> Node:
        return self._query(0, 0, self.n - 1, ql, qr)

    def _query(self, cur: int, l: int, r: int, ql: int, qr: int) -> Node:
        if ql <= l and r <= qr:
            return self.tree[cur]
        
        mid = (l + r) // 2
        if qr <= mid:
            return self._query(2 * cur + 1, l, mid, ql, qr)
        if ql > mid:
            return self._query(2 * cur + 2, mid + 1, r, ql, qr)
            
        left_res = self._query(2 * cur + 1, l, mid, ql, qr)
        right_res = self._query(2 * cur + 2, mid + 1, r, ql, qr)
        return self._merge(left_res, right_res)


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        ans = []
        
        for index, value, start, x in queries:
            tree.update(index, value)
            res_node = tree.query(start, n - 1)
            ans.append(res_node.remain[x])
            
        return ans