class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        s1 = [0] * (2 * size)   # sum of d
        s2 = [0] * (2 * size)   # sum of d^2
        lz = [0] * (2 * size)   # lazy add
        ln = [0] * (2 * size)   # segment length
        for i in range(size):
            ln[size + i] = 1
        for i in range(size - 1, 0, -1):
            ln[i] = ln[2 * i] + ln[2 * i + 1]

        def apply(node, v):
            s2[node] += 2 * v * s1[node] + ln[node] * v * v
            s1[node] += ln[node] * v
            lz[node] += v

        def push(node):
            if lz[node]:
                apply(2 * node, lz[node])
                apply(2 * node + 1, lz[node])
                lz[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, 1)
                return
            push(node)
            m = (l + r) // 2
            if ql <= m:
                update(2 * node, l, m, ql, qr)
            if qr > m:
                update(2 * node + 1, m + 1, r, ql, qr)
            s1[node] = s1[2 * node] + s1[2 * node + 1]
            s2[node] = s2[2 * node] + s2[2 * node + 1]

        last = {}
        ans = 0
        for j, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, size - 1, p + 1, j)
            last[x] = j
            ans += s2[1]
        return ans % MOD