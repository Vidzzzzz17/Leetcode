from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        xs = sorted({x for x, y, l in squares} | {x + l for x, y, l in squares})
        idx = {x: i for i, x in enumerate(xs)}
        m = len(xs) - 1  # number of leaf intervals

        events = []
        for x, y, l in squares:
            a, b = idx[x], idx[x + l]
            events.append((y, 1, a, b))
            events.append((y + l, -1, a, b))
        events.sort()

        cnt = [0] * (4 * m)
        ln = [0] * (4 * m)

        def update(node, lo, hi, l, r, v):
            # node covers leaves [lo, hi)
            if r <= lo or hi <= l:
                return
            if l <= lo and hi <= r:
                cnt[node] += v
            else:
                mid = (lo + hi) // 2
                update(2 * node, lo, mid, l, r, v)
                update(2 * node + 1, mid, hi, l, r, v)
            if cnt[node] > 0:
                ln[node] = xs[hi] - xs[lo]
            elif hi - lo == 1:
                ln[node] = 0
            else:
                ln[node] = ln[2 * node] + ln[2 * node + 1]

        segs = []
        prev_y = events[0][0]
        for y, v, a, b in events:
            if y > prev_y:
                segs.append((prev_y, y, ln[1]))
                prev_y = y
            update(1, 0, m, a, b, v)

        total = sum(w * (y2 - y1) for y1, y2, w in segs)
        half = total / 2

        acc = 0
        for y1, y2, w in segs:
            area = w * (y2 - y1)
            if w > 0 and acc + area >= half:
                return y1 + (half - acc) / w
            acc += area

        return float(prev_y)