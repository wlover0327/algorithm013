class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def temp(lst, nums):
            if not nums:
                result.append(lst)
            else:
                for i, num in enumerate(nums):
                    temp(lst+[num], nums[:i]+nums[i+1:])
        
        
        temp([], nums)
        return result
