from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        self.count -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        by_idx = [(edges[i][2], edges[i][0], edges[i][1], i) for i in range(m)]
        order = sorted(by_idx)

        def mst(skip=-1, force=-1):
            uf = UnionFind(n)
            total = 0
            if force != -1:
                w, a, b, _ = by_idx[force]
                uf.union(a, b)
                total += w
            for w, a, b, i in order:
                if i == skip or i == force:
                    continue
                if uf.union(a, b):
                    total += w
            return total if uf.count == 1 else float('inf')

        base = mst()
        critical, pseudo = [], []
        for i in range(m):
            if mst(skip=i) > base:
                critical.append(i)
            elif mst(force=i) == base:
                pseudo.append(i)
        return [critical, pseudo]