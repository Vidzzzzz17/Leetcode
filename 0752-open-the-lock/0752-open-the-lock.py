from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        visited = {"0000"}
        queue = deque([("0000", 0)])

        while queue:
            state, steps = queue.popleft()
            for i in range(4):
                digit = int(state[i])
                for delta in (1, -1):
                    nd = (digit + delta) % 10
                    nxt = state[:i] + str(nd) + state[i + 1:]
                    if nxt in dead or nxt in visited:
                        continue
                    if nxt == target:
                        return steps + 1
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
        return -1