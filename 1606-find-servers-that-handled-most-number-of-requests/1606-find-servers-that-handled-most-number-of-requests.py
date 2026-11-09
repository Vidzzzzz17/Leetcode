import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))          # virtual indices; heap property holds since sorted
        busy = []                      # (end_time, virtual_index)
        count = [0] * k

        for i, (t, l) in enumerate(zip(arrival, load)):
            # release servers that have finished
            while busy and busy[0][0] <= t:
                _, v = heapq.heappop(busy)
                # smallest virtual index >= i congruent to v (mod k)
                nv = i + ((v - i) % k)
                heapq.heappush(free, nv)

            if not free:
                continue                # dropped

            v = heapq.heappop(free)
            s = v % k
            count[s] += 1
            heapq.heappush(busy, (t + l, v))

        m = max(count)
        return [s for s in range(k) if count[s] == m]