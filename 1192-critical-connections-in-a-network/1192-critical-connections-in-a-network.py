from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        disc = [-1] * n
        low = [0] * n
        res = []
        timer = 0

        # stack frames: (node, parent, index of next neighbor to visit)
        disc[0] = low[0] = timer
        timer += 1
        stack = [(0, -1, 0)]

        while stack:
            u, parent, i = stack.pop()
            if i < len(graph[u]):
                # come back to u later to process the next neighbor
                stack.append((u, parent, i + 1))
                v = graph[u][i]
                if v == parent:
                    continue
                if disc[v] == -1:
                    disc[v] = low[v] = timer
                    timer += 1
                    stack.append((v, u, 0))
                else:
                    low[u] = min(low[u], disc[v])
            else:
                # u is finished: propagate its low value to the parent
                if parent != -1:
                    low[parent] = min(low[parent], low[u])
                    if low[u] > disc[parent]:
                        res.append([parent, u])
        return res