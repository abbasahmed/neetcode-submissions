class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            filtered = [num for j, num in enumerate(nums) if i != j]
            prod = 1
            for j in filtered:
                prod *= j
            res[i] = prod
        
        return res