class Solution:

    def encode(self, strs: List[str]) -> str:
        the_word = ""
        for s in strs:
            word_len = len(s)
            the_word += f"{word_len}#{s}"

        return the_word    

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []
        while i < len(s):

            j = s.find("#" , i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)

            i = j + 1 + length

        return res    
