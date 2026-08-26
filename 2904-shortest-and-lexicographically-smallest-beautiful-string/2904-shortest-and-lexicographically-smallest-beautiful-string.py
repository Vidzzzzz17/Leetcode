class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Store indices of all '1's in the string
        ones = [i for i, char in enumerate(s) if char == '1']
        
        # If there are fewer than k ones, no beautiful substring can exist
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        best_sub = ""
        
        # Check every window of k ones
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            
            current_len = end - start + 1
            sub = s[start:end + 1]
            
            # Prefer shorter lengths, or lexicographically smaller strings of the same length
            if current_len < min_len:
                min_len = current_len
                best_sub = sub
            elif current_len == min_len:
                if sub < best_sub:
                    best_sub = sub
                    
        return best_sub