class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
        curr_min = float("inf")
        
        while start < end:
            mid = (end + start) // 2
            curr_min = min(curr_min, nums[mid])
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1
        
        return nums[start]

