import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        K = k + 1
        INF = float('inf')
        # dist[v * K + r], r in 1..k
        dist = [INF] * (n * K)
        dist[1] = 0  # node 0, run length 1
        pq = [(0, 0, 1)]

        while pq:
            d, u, r = heapq.heappop(pq)
            if d > dist[u * K + r]:
                continue
            if u == n - 1:
                return d
            lu = labels[u]
            for v, w in adj[u]:
                if labels[v] == lu:
                    nr = r + 1
                    if nr > k:
                        continue
                else:
                    nr = 1
                nd = d + w
                idx = v * K + nr
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(pq, (nd, v, nr))
        return -1