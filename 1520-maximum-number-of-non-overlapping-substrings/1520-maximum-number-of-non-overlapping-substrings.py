class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find the first and last occurrences of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        valid_intervals = []

        # Step 2: Try to form a valid valid interval starting at the first occurrence of each character
        for ch in first:
            i = first[ch]
            j = last[ch]
            is_valid = True
            k = i
            
            while k <= j:
                # Expand the right boundary if needed
                if last[s[k]] > j:
                    j = last[s[k]]
                # If a character's first occurrence is before our starting point 'i', 
                # 'i' cannot be the start of a valid minimal substring.
                if first[s[k]] < i:
                    is_valid = False
                    break
                k += 1
            
            if is_valid:
                valid_intervals.append((i, j))

        # Step 3: Sort valid intervals by their end position (j)
        valid_intervals.sort(key=lambda x: x[1])

        # Step 4: Greedily pick non-overlapping intervals
        res = []
        last_end = -1

        for i, j in valid_intervals:
            if i > last_end:
                res.append(s[i : j + 1])
                last_end = j

        return res