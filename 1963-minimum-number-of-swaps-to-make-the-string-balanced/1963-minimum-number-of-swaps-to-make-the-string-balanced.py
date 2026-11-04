class Solution:
    def minSwaps(self, s: str) -> int:
        open_cnt = 0
        unmatched = 0
        for ch in s:
            if ch == '[':
                open_cnt += 1
            elif open_cnt > 0:
                open_cnt -= 1
            else:
                unmatched += 1
        return (unmatched + 1) // 2