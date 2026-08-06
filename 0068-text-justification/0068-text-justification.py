class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        current_line = []
        current_length = 0
        
        for word in words:
            # Check if adding this word (plus a space) would exceed maxWidth
            if current_length + len(current_line) + len(word) > maxWidth:
                result.append(self._justify_line(current_line, current_length, maxWidth))
                current_line = []
                current_length = 0
            
            current_line.append(word)
            current_length += len(word)
        
        # Last line: left-justified, single space between words, padded on the right
        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
    
    def _justify_line(self, words: list[str], total_char_length: int, maxWidth: int) -> str:
        if len(words) == 1:
            # Single word: left-justify, pad right with spaces
            return words[0] + ' ' * (maxWidth - total_char_length)
        
        total_spaces = maxWidth - total_char_length
        gaps = len(words) - 1
        space_per_gap = total_spaces // gaps
        extra_spaces = total_spaces % gaps
        
        line = ''
        for i, word in enumerate(words[:-1]):
            line += word
            spaces = space_per_gap + (1 if i < extra_spaces else 0)
            line += ' ' * spaces
        line += words[-1]
        
        return line