class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)  # stands in for a mutable char array
        n = len(chars)

        def reverse(lo: int, hi: int) -> None:
            while lo < hi:
                chars[lo], chars[hi] = chars[hi], chars[lo]
                lo += 1
                hi -= 1

        # Step 1: compact the array, keeping single spaces between words only
        write = 0
        read = 0
        while read < n:
            if chars[read] != ' ':
                if write != 0:
                    chars[write] = ' '
                    write += 1
                while read < n and chars[read] != ' ':
                    chars[write] = chars[read]
                    write += 1
                    read += 1
            else:
                read += 1
        length = write

        # Step 2: reverse the whole cleaned string
        reverse(0, length - 1)

        # Step 3: reverse each word back to normal
        start = 0
        for i in range(length + 1):
            if i == length or chars[i] == ' ':
                reverse(start, i - 1)
                start = i + 1

        return "".join(chars[:length])