class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []

        close_To_Open = {")": "(", "]": "[", "}": "{"}

        for char in s :
            if char in close_To_Open:
                if stack and stack[-1] == close_To_Open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)            
        
        return True if not stack else False