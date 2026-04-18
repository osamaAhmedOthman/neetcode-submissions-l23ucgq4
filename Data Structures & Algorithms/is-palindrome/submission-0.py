class Solution:
    def isPalindrome(self, s: str) -> bool:
        
       clean_s = ""
       i=0
       
       for letter in s:
            if letter.isalnum():
                clean_s += letter.lower()
        
       length = len(clean_s) // 2 
       while i < length:
            if clean_s[i] != clean_s[len(clean_s) - 1 - i]:
                return False
            i += 1

       return True    