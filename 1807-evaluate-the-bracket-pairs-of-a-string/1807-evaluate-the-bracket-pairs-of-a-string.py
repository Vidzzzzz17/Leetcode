from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Convert knowledge list to a dictionary for O(1) lookups
        knowledge_dict = {k: v for k, v in knowledge}
        
        result = []
        current_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(current_key)
                # Lookup the key, default to "?" if not found
                result.append(knowledge_dict.get(key_str, "?"))
                current_key = []  # Reset the key buffer
            elif in_bracket:
                current_key.append(char)
            else:
                result.append(char)
                
        return "".join(result)