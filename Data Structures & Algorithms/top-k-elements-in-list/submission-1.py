class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_map = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in count_map:
                count_map[n] += 1
            else: count_map[n] = 1

        for num , count in count_map.items():
            buckets[count].append(num)        

        result = []

        for i in range(len(nums) , 0 , -1):
            result += buckets[i]
            if len(result) == k:
                break

        return result[0:k]        