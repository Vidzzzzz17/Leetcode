from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        # Check if prefix target[0...i-1] can be formed using s
        def is_valid_prefix(p_counts):
            return all(p_counts[c] <= total_counts[c] for c in p_counts)

        # Try prefix lengths from n-1 down to 0
        for i in range(n - 1, -1, -1):
            prefix_counts = Counter(target[:i])
            
            if not is_valid_prefix(prefix_counts):
                continue
            
            # Available characters remaining after creating prefix target[0...i-1]
            remaining = total_counts - prefix_counts
            
            # Find the smallest character strictly greater than target[i]
            target_char = target[i]
            chosen_char = None
            for char_code in range(ord(target_char) + 1, ord('z') + 1):
                c = chr(char_code)
                if remaining[c] > 0:
                    chosen_char = c
                    break
            
            # Construct the result if a valid split point is found
            if chosen_char:
                remaining[chosen_char] -= 1
                
                # Append remaining characters in ascending sorted order
                suffix = "".join(c * remaining[c] for c in sorted(remaining.keys()))
                return target[:i] + chosen_char + suffix
                
        return ""