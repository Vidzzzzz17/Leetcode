/*
There is a robot on an m x n grid. The robot is initially located at 
the top-left corner (i.e., grid[0][0]). The robot tries to move to the 
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move 
either down or right at any point in time.
*/

int uniquePaths(int m, int n) {
    int total_steps = m + n - 2;
    int k = (m - 1 < n - 1) ? m - 1 : n - 1;
    
    long long result = 1;
    
    for (int i = 1; i <= k; i++) {
        result = result * (total_steps - k + i) / i;
    }
    
    return (int)result;
}