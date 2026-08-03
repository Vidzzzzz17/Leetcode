class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current: list[str]) -> None:
            # Base case: combination is complete
            if index == len(digits):
                result.append(''.join(current))
                return
            
            letters = phone_map[digits[index]]
            for letter in letters:
                current.append(letter)
                backtrack(index + 1, current)
                current.pop()  # undo the choice, try the next letter
        
        backtrack(0, [])
        return result
        