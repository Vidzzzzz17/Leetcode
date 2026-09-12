#include <vector>
#include <algorithm>

using namespace std;

struct Interval {
    long long l, r, weight;
    int id;
};

struct DPValue {
    long long weight = 0;
    vector<int> indices;

    bool operator<(const DPValue& other) const {
        if (weight != other.weight) {
            return weight < other.weight;
        }
        // For equal weight, prefer lexicographically smaller indices
        return indices > other.indices;
    }
};

class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<Interval> sorted_intervals(n);
        
        for (int i = 0; i < n; ++i) {
            sorted_intervals[i] = {intervals[i][0], intervals[i][1], intervals[i][2], i};
        }
        
        // Sort intervals primarily by left endpoint
        sort(sorted_intervals.begin(), sorted_intervals.end(), [](const Interval& a, const Interval& b) {
            if (a.l != b.l) return a.l < b.l;
            if (a.r != b.r) return a.r < b.r;
            if (a.weight != b.weight) return a.weight > b.weight;
            return a.id < b.id;
        });

        vector<long long> left_bounds(n);
        for (int i = 0; i < n; ++i) {
            left_bounds[i] = sorted_intervals[i].l;
        }

        // dp[i][k] stores the best DPValue choosing at most k intervals from suffix i..n-1
        vector<vector<DPValue>> dp(n + 1, vector<DPValue>(5));

        for (int i = n - 1; i >= 0; --i) {
            // Binary search for the first interval starting strictly after sorted_intervals[i].r
            int next_idx = upper_bound(left_bounds.begin(), left_bounds.end(), sorted_intervals[i].r) - left_bounds.begin();

            for (int k = 1; k <= 4; ++k) {
                // Option 1: Skip interval i
                DPValue best = dp[i + 1][k];

                // Option 2: Take interval i
                DPValue take;
                take.weight = sorted_intervals[i].weight + dp[next_idx][k - 1].weight;
                take.indices = dp[next_idx][k - 1].indices;
                take.indices.push_back(sorted_intervals[i].id);
                
                // Keep indices sorted for correct lexicographical comparison
                sort(take.indices.begin(), take.indices.end());

                if (best < take) {
                    best = take;
                }
                
                dp[i][k] = best;
            }
        }

        return dp[0][4].indices;
    }
};