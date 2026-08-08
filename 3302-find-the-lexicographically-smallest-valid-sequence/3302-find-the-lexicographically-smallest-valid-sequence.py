class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)
        if m > n:
            return []

        # suf[i] = smallest j such that word2[j:] is a subsequence of word1[i:]
        suf = [0] * (n + 1)
        suf[n] = m
        j = m
        for i in range(n - 1, -1, -1):
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
            suf[i] = j

        result = []
        i = jj = 0
        mismatch_used = False

        while i < n and jj < m:
            if word1[i] == word2[jj]:
                result.append(i)
                i += 1
                jj += 1
            else:
                if not mismatch_used and suf[i + 1] <= jj + 1:
                    result.append(i)
                    mismatch_used = True
                    i += 1
                    jj += 1
                else:
                    i += 1

        if jj < m:
            return []
        return result