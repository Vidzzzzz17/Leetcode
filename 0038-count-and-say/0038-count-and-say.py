class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        
        for _ in range(2, n + 1):
            next_str = []
            i = 0
            
            while i < len(current):
                count = 1
                while i + 1 < len(current) and current[i] == current[i + 1]:
                    i += 1
                    count += 1
                
                next_str.append(str(count))
                next_str.append(current[i])
                i += 1
            
            current = "".join(next_str)
        
        return current