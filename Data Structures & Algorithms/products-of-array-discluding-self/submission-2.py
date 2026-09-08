class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        res = [1] * len(nums)
        if zero_cnt > 1: return [0] * len(nums)
        for i, n in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if n != 0 else prod
            else:
                res[i] = prod // n
        return res
