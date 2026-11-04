class Solution:
    def rand10(self):
        while True:
            idx = (rand7() - 1) * 7 + rand7()
            if idx <= 40:
                return (idx - 1) % 10 + 1