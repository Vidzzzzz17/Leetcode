class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort intervals based on their start times
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If merged is empty or if current interval does not overlap with the previous, append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, merge the current interval with the previous one
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged