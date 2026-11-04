class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        # dp maps diff (left - right) to max left height
        dp = {0: 0}
        
        for r in rods:
            curr = list(dp.items())
            for diff, left in curr:
                right = left - diff
                
                # Option 1: Add rod to the left support
                new_diff_1 = diff + r
                dp[new_diff_1] = max(dp.get(new_diff_1, 0), left + r)
                
                # Option 2: Add rod to the right support
                new_diff_2 = abs(diff - r)
                if diff >= r:
                    new_left_2 = left
                else:
                    new_left_2 = right + r
                dp[new_diff_2] = max(dp.get(new_diff_2, 0), new_left_2)
                
        return dp.get(0, 0)