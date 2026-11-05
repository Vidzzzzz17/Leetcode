class Solution:
    def maxStability(self, n, edges, k):
        def find(p, a):
            while p[a] != a:
                p[a] = p[p[a]]
                a = p[a]
            return a

        # mandatory cycle check
        p = list(range(n))
        for u, v, s, m in edges:
            if m:
                a, b = find(p, u), find(p, v)
                if a == b:
                    return -1
                p[a] = b

        def feasible(x):
            p = list(range(n))
            comps = n
            for u, v, s, m in edges:
                if m:
                    if s < x:
                        return False
                    a, b = find(p, u), find(p, v)
                    p[a] = b
                    comps -= 1
            for u, v, s, m in edges:
                if not m and s >= x:
                    a, b = find(p, u), find(p, v)
                    if a != b:
                        p[a] = b
                        comps -= 1
            used = 0
            for u, v, s, m in edges:
                if not m and s < x <= 2 * s:
                    a, b = find(p, u), find(p, v)
                    if a != b:
                        p[a] = b
                        comps -= 1
                        used += 1
                        if used > k:
                            return False
            return comps == 1

        lo, hi, ans = 1, 200000, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans