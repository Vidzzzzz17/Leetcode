class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        s_idx, p_idx = 0, 0
        match_idx = 0
        star_idx = -1

        while s_idx < len(s):
            # Case 1: Direct match or '?' wildcard
            if p_idx < len(p) and (
                p[p_idx] == "?" or p[p_idx] == s[s_idx]
            ):
                s_idx += 1
                p_idx += 1

            # Case 2: Encounter '*', record positions and assume empty match for now
            elif p_idx < len(p) and p[p_idx] == "*":
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1

            # Case 3: Mismatch occurs, but we previously saw a '*' -> Backtrack
            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx

            # Case 4: Mismatch with no previous '*'
            else:
                return False

        # Consume remaining '*' characters in pattern
        while p_idx < len(p) and p[p_idx] == "*":
            p_idx += 1

        return p_idx == len(p)