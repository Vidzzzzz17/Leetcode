from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)
        
        if n < total_len:
            return []
        
        word_freq = Counter(words)
        result = []
        
        # We only need to check starting offsets from 0 to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            count = 0
            
            while right + word_len <= n:
                # Extract the word at the right end of the window
                w = s[right:right + word_len]
                right += word_len
                
                if w in word_freq:
                    current_count[w] += 1
                    count += 1
                    
                    # If word count exceeds required frequency, shrink window from left
                    while current_count[w] > word_freq[w]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If all words match, record the start index
                    if count == word_count:
                        result.append(left)
                else:
                    # Reset window if word is invalid
                    current_count.clear()
                    count = 0
                    left = right
                    
        return result