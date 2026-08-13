from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        
        # Segment tree node arrays
        # size, pref, suf, best (all lengths), leftChar, rightChar
        size_ = [0] * (4 * n)
        pref = [0] * (4 * n)
        suf = [0] * (4 * n)
        best = [0] * (4 * n)
        leftChar = [''] * (4 * n)
        rightChar = [''] * (4 * n)
        
        def merge(node, l, r, mid):
            lc, rc = 2 * node, 2 * node + 1
            size_[node] = size_[lc] + size_[rc]
            leftChar[node] = leftChar[lc]
            rightChar[node] = rightChar[rc]
            
            if leftChar[lc] == rightChar[rc]:
                # only matters for connecting middle boundary, handled below
                pass
            
            # prefix
            if pref[lc] == size_[lc] and rightChar[lc] == leftChar[rc]:
                pref[node] = size_[lc] + pref[rc]
            else:
                pref[node] = pref[lc]
            
            # suffix
            if suf[rc] == size_[rc] and leftChar[rc] == rightChar[lc]:
                suf[node] = size_[rc] + suf[lc]
            else:
                suf[node] = suf[rc]
            
            # best
            mid_combine = 0
            if rightChar[lc] == leftChar[rc]:
                mid_combine = suf[lc] + pref[rc]
            best[node] = max(best[lc], best[rc], mid_combine)
        
        def build(node, l, r):
            if l == r:
                size_[node] = 1
                pref[node] = 1
                suf[node] = 1
                best[node] = 1
                leftChar[node] = s[l]
                rightChar[node] = s[l]
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            merge(node, l, r, mid)
        
        def update(node, l, r, idx, ch):
            if l == r:
                s[idx] = ch
                leftChar[node] = ch
                rightChar[node] = ch
                # size, pref, suf, best remain 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            merge(node, l, r, mid)
        
        if n > 0:
            build(1, 0, n - 1)
        
        k = len(queryCharacters)
        result = [0] * k
        for i in range(k):
            idx = queryIndices[i]
            ch = queryCharacters[i]
            if s[idx] != ch:
                update(1, 0, n - 1, idx, ch)
            result[i] = best[1]
        
        return result
        