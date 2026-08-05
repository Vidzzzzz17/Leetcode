class Solution:

    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        # We don't need to process the last element because reaching or surpassing
        # n - 1 is the objective.
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            # When we reach the end of the current jump boundary:
            if i == current_end:
                jumps += 1
                current_end = farthest

                # Early stop if we can already reach the last index
                if current_end >= n - 1:
                    break

        return jumps