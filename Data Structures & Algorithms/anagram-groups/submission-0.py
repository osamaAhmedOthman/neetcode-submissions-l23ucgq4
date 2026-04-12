from abc import abstractproperty
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)

            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]    

        return list(anagram_map.values())        