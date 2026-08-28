class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left_sum, left_q = 0, 0
        right_sum, right_q = 0, 0
        
        # Calculate sums and '?' counts for both halves
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
                
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
                
        # Condition 1: If total '?' is odd, Alice always wins
        if (left_q + right_q) % 2 != 0:
            return True
            
        # Condition 2: Bob wins if and only if:
        # left_sum - right_sum == 9 * (right_q - left_q) // 2
        return (left_sum - right_sum) != 9 * (right_q - left_q) // 2