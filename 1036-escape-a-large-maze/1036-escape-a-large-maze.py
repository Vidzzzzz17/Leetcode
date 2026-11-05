from collections import deque
from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True

        N = 10**6
        blocked_set = {(x, y) for x, y in blocked}
        n = len(blocked)
        limit = n * (n - 1) // 2

        def bfs(start, goal):
            # True if we reach `goal` or escape (visit more than `limit` cells)
            start = tuple(start)
            goal = tuple(goal)
            visited = {start}
            queue = deque([start])
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < N and 0 <= ny < N):
                        continue
                    nxt = (nx, ny)
                    if nxt in visited or nxt in blocked_set:
                        continue
                    if nxt == goal:
                        return True
                    visited.add(nxt)
                    if len(visited) > limit:
                        return True
                    queue.append(nxt)
            return False

        return bfs(source, target) and bfs(target, source)