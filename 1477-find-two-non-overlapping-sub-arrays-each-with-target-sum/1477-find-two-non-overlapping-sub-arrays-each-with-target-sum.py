class Solution:

    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float("inf")

        # min_len[i] stores the min length of a valid subarray ending at or before index i
        min_len = [INF] * n

        prefix_map = {0: -1}
        curr_sum = 0
        ans = INF
        best_so_far = INF

        for i in range(n):
            curr_sum += arr[i]

            # Check if there is a subarray ending at index i with sum equal to target
            if (curr_sum - target) in prefix_map:
                prev_idx = prefix_map[curr_sum - target]
                length = i - prev_idx

                # If a valid non-overlapping subarray exists before prev_idx
                if prev_idx >= 0 and min_len[prev_idx] != INF:
                    ans = min(ans, length + min_len[prev_idx])

                best_so_far = min(best_so_far, length)

            min_len[i] = best_so_far
            prefix_map[curr_sum] = i

        return ans if ans != INF else -1