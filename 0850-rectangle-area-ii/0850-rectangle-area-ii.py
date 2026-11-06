from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        xs = sorted({x for r in rectangles for x in (r[0], r[2])})
        total = 0

        for i in range(len(xs) - 1):
            x_lo, x_hi = xs[i], xs[i + 1]
            # y-intervals of rectangles covering this whole strip
            intervals = sorted(
                (r[1], r[3]) for r in rectangles
                if r[0] <= x_lo and r[2] >= x_hi
            )

            covered = 0
            cur_start = cur_end = None
            for y1, y2 in intervals:
                if cur_end is None or y1 > cur_end:
                    if cur_end is not None:
                        covered += cur_end - cur_start
                    cur_start, cur_end = y1, y2
                else:
                    cur_end = max(cur_end, y2)
            if cur_end is not None:
                covered += cur_end - cur_start

            total += covered * (x_hi - x_lo)

        return total % MOD
        