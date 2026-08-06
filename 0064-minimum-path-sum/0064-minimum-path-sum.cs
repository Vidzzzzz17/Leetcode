using System;

public class Solution {
    public int MinPathSum(int[][] grid) {
        int m = grid.Length;
        int n = grid[0].Length;

        // 1D DP array to optimize space to O(n)
        int[] dp = new int[n];

        // Base case: top-left cell
        dp[0] = grid[0][0];

        // Initialize the first row
        for (int j = 1; j < n; j++) {
            dp[j] = dp[j - 1] + grid[0][j];
        }

        // Fill DP array row by row
        for (int i = 1; i < m; i++) {
            // First column can only come from above
            dp[0] += grid[i][0];

            for (int j = 1; j < n; j++) {
                // Min path sum coming from above (dp[j]) vs left (dp[j - 1])
                dp[j] = grid[i][j] + Math.Min(dp[j], dp[j - 1]);
            }
        }

        return dp[n - 1];
    }
}