class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev = s[::-1]
        combined = s + '#' + rev
        n = len(combined)
        
        # KMP failure function
        fail = [0] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = fail[j - 1]
            if combined[i] == combined[j]:
                j += 1
            fail[i] = j
        
        # fail[-1] = length of longest prefix of s that is also a palindrome
        longest_palindrome_prefix_len = fail[-1]
        to_add = s[longest_palindrome_prefix_len:][::-1]
        
        return to_add + s