class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        res = []

        for i , a  in enumerate(nums):         
            if i > 0 and a == nums[i-1]:
                continue

            j , k = i+1 , len(nums)-1
            while j < k:
                three_sum = a + nums[j] + nums[k]

                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else: 
                    res.append([a , nums[j] , nums[k]])        

                    j +=1 
                    while j < k and nums[j] == nums[j-1]:
                         j+=1
        return res

