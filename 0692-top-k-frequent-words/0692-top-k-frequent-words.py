from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        return sorted(count, key=lambda w: (-count[w], w))[:k]