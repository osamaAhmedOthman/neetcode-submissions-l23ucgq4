class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        our_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in our_dict:
                return[our_dict[complement] , i]
            else:
                our_dict[nums[i]] = i    
            