class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}

        for n in nums:
            if n in count_map:
                count_map[n] +=1
            else: count_map[n] = 1    

        sorted_keys = sorted(count_map.keys(), key=count_map.get, reverse=True)

        return sorted_keys[0:k]

