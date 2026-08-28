from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        counts = Counter(s)
        
        # Check palindrome feasibility
        odd_chars = [c for c, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid = odd_chars[0] if odd_chars else ""
        
        # Available character pool for the first half
        half_counts = {c: counts[c] // 2 for c in sorted(counts.keys())}
        
        # Helper to check if a prefix can be matched using current available half_counts
        def can_form_prefix(prefix_len):
            temp_counts = half_counts.copy()
            for k in range(prefix_len):
                char = target[k]
                if temp_counts.get(char, 0) <= 0:
                    return None
                temp_counts[char] -= 1
            return temp_counts

        # Helper to build full palindrome given first half string
        def make_palindrome(first_half):
            if n % 2 == 1:
                return first_half + mid + first_half[::-1]
            return first_half + first_half[::-1]

        ans = None

        # Try matching target's first half up to index i-1, and taking a strictly larger char at index i
        for i in range(m - 1, -1, -1):
            rem_counts = can_form_prefix(i)
            if rem_counts is None:
                continue
                
            target_char = target[i]
            
            # Try finding the smallest valid character strictly greater than target[i]
            for c in sorted(rem_counts.keys()):
                if c > target_char and rem_counts[c] > 0:
                    curr_rem = rem_counts.copy()
                    curr_rem[c] -= 1
                    
                    # Build rest of the half in sorted ascending order
                    first_half = target[:i] + c
                    for char in sorted(curr_rem.keys()):
                        first_half += char * curr_rem[char]
                    
                    candidate = make_palindrome(first_half)
                    if candidate > target:
                        if ans is None or candidate < ans:
                            ans = candidate
                    break

        # Check matching the entire first half of target
        rem_counts = can_form_prefix(m)
        if rem_counts is not None:
            first_half = target[:m]
            candidate = make_palindrome(first_half)
            if candidate > target:
                if ans is None or candidate < ans:
                    ans = candidate

        return ans if ans is not None else ""