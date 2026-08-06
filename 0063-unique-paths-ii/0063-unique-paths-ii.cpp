#include <vector>

class Solution {
public:
    int uniquePathsWithObstacles(std::vector<std::vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();

        // Edge case: If starting cell or destination has an obstacle
        if (obstacleGrid[0][0] == 1 || obstacleGrid[m - 1][n - 1] == 1) {
            return 0;
        }

        // Use 1D vector to optimize space to O(n)
        // Using long long to prevent potential intermediate integer overflow
        std::vector<long long> dp(n, 0);
        
        // Start position
        dp[0] = 1;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0; // Obstacle blocks all paths through this cell
                } else if (j > 0) {
                    dp[j] += dp[j - 1]; // Current paths = paths from top + paths from left
                }
            }
        }

        return static_cast<int>(dp[n - 1]);
    }
};