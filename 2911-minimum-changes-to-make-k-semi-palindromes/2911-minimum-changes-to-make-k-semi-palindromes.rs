
impl Solution {
    pub fn minimum_changes(s: String, k: i32) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        let k = k as usize;
        let inf = 1_000_000_000;

        // Step 1: Precompute proper divisors
        let mut divisors = vec![Vec::new(); n + 1];

        for len in 2..=n {
            for d in 1..len {
                if len % d == 0 {
                    divisors[len].push(d);
                }
            }
        }

        // Step 2: Precompute substring costs
        let mut cost = vec![vec![inf; n]; n];

        for i in 0..n {
            for j in (i + 1)..n {
                let len = j - i + 1;

                for &d in &divisors[len] {
                    let mut changes = 0;

                    for offset in 0..d {
                        let mut left = i + offset;
                        let mut right =
                            i + offset + (len / d - 1) * d;

                        while left < right {
                            if s[left] != s[right] {
                                changes += 1;
                            }

                            left += d;
                            right -= d;
                        }
                    }

                    cost[i][j] = cost[i][j].min(changes);
                }
            }
        }

        // Step 3: Dynamic programming
        let mut dp = vec![vec![inf; n + 1]; k + 1];
        dp[0][0] = 0;

        for parts in 1..=k {
            for end in (2 * parts)..=n {
                for start in (2 * (parts - 1))..=(end - 2) {
                    dp[parts][end] = dp[parts][end].min(
                        dp[parts - 1][start]
                            + cost[start][end - 1]
                    );
                }
            }
        }

        dp[k][n]
    }
}

