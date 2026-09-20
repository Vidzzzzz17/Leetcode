class Solution:

    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        for idx, char in enumerate(s, start=1):
            # Calculate position in reversed alphabet ('a' -> 26, 'z' -> 1)
            rev_alphabet_idx = 26 - (ord(char) - ord("a"))
            total_degree += rev_alphabet_idx * idx
        return total_degree